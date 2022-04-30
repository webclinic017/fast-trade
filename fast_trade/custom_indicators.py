from finta.finta import inputvalidator, apply
from pandas import DataFrame, Series
import finta
from numpy import log10 as npLog10
from numpy import log as npLn

@apply(inputvalidator(input_="ohlc"))
def choppiness_indicator(ohlc: DataFrame, period: int = 14, ln=False, scaler=100) -> Series:
    """
    Calculate choppiness indicator.

    :param ohlc: OHLC dataframe.
    :return: Dataframe with choppiness indicator.
    """
    # copilot wrote this!
    # return ohlc.apply(lambda x: x["high"] - x["low"]) / (
    #     ohlc.apply(lambda x: x["high"] - x["low"]).rolling(window=20).mean()
    # )

    # caclulate the atr
    atr = finta.TA.ATR(ohlc, period=period)
    atr_sum = atr.rolling(window=period).sum()

    # get the difference between the high and low
    diff = ohlc["high"].rolling(window=period).max() - ohlc["low"].rolling(window=period).min()

    if ln:
        chop = 100 * (npLn(atr_sum) - npLn(diff)) / npLn(period)
    else:
        chop = 100* (npLog10(atr_sum) - npLog10(diff)) / npLog10(period)

    return chop


