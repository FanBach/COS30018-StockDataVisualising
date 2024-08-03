import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from mplfinance.original_flavor import candlestick_ohlc

from dataProcessing import *


def plotSingleFeature(predictionName, actualData, predictedData):
    plt.figure(figsize=(16, 9))
    plt.title(predictionName)
    plt.plot(actualData, label="Actual Prices", color="blue")
    plt.plot(predictedData, label="Predicted Prices", color="orange")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

