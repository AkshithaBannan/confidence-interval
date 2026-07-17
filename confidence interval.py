# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:10:03 2024

@author: excel
"""

import pandas as pd
df = pd.read_csv("Lungcapdata.csv")
df

df["LungCap"].mean()

from scipy.stats import norm
lungcap_90 = norm.interval(0.90, loc=df["LungCap"].mean(), scale=df["LungCap"].std())
lungcap_90

# i am 90% confident that population mean vlaue of lungcap data is falls under above interval

lungcap_95 = norm.interval(0.95, loc=df["LungCap"].mean(), scale=df["LungCap"].std())
lungcap_95

# i am 95% confident that population mean vlaue of lungcap data is falls under above interval

lungcap_99 = norm.interval(0.99, loc=df["LungCap"].mean(), scale=df["LungCap"].std())
lungcap_99

# i am 99% confident that population mean vlaue of lungcap data is falls under above interval


#===============================================================================


