# Nạp thư viện để sử dụng
from vnstock import Vnstock
import pandas as pd

stock_symbol = 'VCB'
stock_source = 'VCI'

# Định nghĩa biến vnstock lưu thông tin mã chứng khoán & nguồn dữ liệu bạn sử dụng
stock = Vnstock().stock(symbol=stock_symbol, source=stock_source)

# Thiết lập thời gian tải dữ liệu và khung thời gian tra cứu là 1 ngày
df = stock.quote.history(start='2025-04-01', end='2025-05-21', interval='1D')

# Lưu dữ liệu thô vào thư mục ../data/raw/
raw_file_name = 'raw_data_' + stock_symbol + '_' + stock_source
raw_file_path = '../data/raw/' + raw_file_name + '.csv'
df.to_csv(raw_file_path, index=False)

# Làm sạch dữ liệu bằng pandas
def clean_data(dataframe):
    # Loại bỏ các hàng có giá trị NaN
    df_cleaned = dataframe.dropna()

    # Loại bỏ các cột không cần thiết (giả sử cột 'time' không cần thiết)
    df_cleaned = df_cleaned.drop(columns=['time'])

    # Chỉ lấy các cột cần thiết
    df_cleaned = df_cleaned[['open', 'high', 'low', 'close', 'volume']]

    return df_cleaned

# Tạo đặc trưng kỹ thuật
def create_technical_features(dataframe):
    # SMA (Simple Moving Average)
    dataframe['SMA_20'] = dataframe['close'].rolling(window=20).mean()

    # EMA (Exponential Moving Average)
    dataframe['EMA_20'] = dataframe['close'].ewm(span=20, adjust=False).mean()

    # RSI (Relative Strength Index)
    delta = dataframe['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    dataframe['RSI_14'] = 100 - (100 / (1 + rs))

    # Các phép tính SMA/EMA/RSI sẽ sinh ra giá trị NaN ở đầu chuỗi, ta cần loại bỏ
    dataframe = dataframe.dropna()

    return dataframe

# Làm sạch và tạo đặc trưng cho dữ liệu
df_cleaned = clean_data(df)
df_processed = create_technical_features(df_cleaned)

# Hiển thị 5 dòng dữ liệu đầu tiên sau khi làm sạch và tạo đặc trưng
print(df_processed.head())

# Lưu dữ liệu đã xử lý vào thư mục ../data/processed/
processed_file_name = 'processed_data_' + stock_symbol + '_' + stock_source
processed_file_path = '../data/processed/' + processed_file_name + '.csv'
df_processed.to_csv(processed_file_path, index=False)