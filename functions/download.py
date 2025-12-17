import pandas as pd
import yfinance as yf


def download_data(ticker: str = 'TSLA') -> pd.DataFrame:
    """Download historical market data for a given ticker from Yahoo Finance.

    Parameters
    ----------
    ticker : str, optional
        The ticker symbol to download data for (default is 'TSLA').

    Returns
    -------
    pd.DataFrame
        A DataFrame containing historical market data (Date, Open, High, Low,
        Close, Volume, etc.). The index is reset so the 'Date' is a column.
    """
    result = yf.download(ticker, period='max', multi_level_index=False).reset_index()
    return result
