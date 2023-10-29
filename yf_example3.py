"""
A function to download stock prices during a given year from Yahoo Finance.
"""
import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """Download Qantas stock prices for a given year into a CSV file

    Parameters
    ----------
     year : int

    Returns
    -------
    Generate a csv file
    """
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, f'qan_stk_{year}.csv')
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    yf_example2.yf_prc_to_csv(tic, pth, start=start, end=end)

if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)