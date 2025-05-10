# PyStockPredict

PyStockPredict is a Python-based project designed to fetch, clean, and analyze stock data using various technical indicators. The project leverages the `vnstock` library to retrieve stock data and `pandas` for data manipulation and analysis.

## Features

- **Data Retrieval**: Fetches historical stock data using the `vnstock` library.
- **Data Cleaning**: Cleans the data by removing NaN values and unnecessary columns.
- **Technical Indicators**: Calculates technical indicators such as Simple Moving Average (SMA), Exponential Moving Average (EMA), and Relative Strength Index (RSI).
- **Data Storage**: Saves raw and processed data to CSV files for further analysis.

## Prerequisites

- Python 3.x
- `vnstock` library
- `pandas` library

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd PyStockPredict
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Main Script:**

   Execute the main script to fetch, clean, and process stock data:

   ```bash
   python src/main.py
   ```

2. **View Processed Data:**

   Processed data will be saved in the `data/processed/` directory as a CSV file.

## Project Structure

- `src/`: Contains the main Python scripts for data loading and processing.
- `data/`: Directory for storing raw and processed data.
- `venv/`: Virtual environment directory (ignored in version control).
- `requirements.txt`: Lists the Python packages required for the project.

## License

This project is licensed under the MIT License.

## Acknowledgments

- The `vnstock` library for providing easy access to stock data.
- The `pandas` library for powerful data manipulation capabilities.
# PyStockPredict
