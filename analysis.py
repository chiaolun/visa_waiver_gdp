#!/usr/bin/env python

import pandas as pd

visa_free = pd.read_csv("visa_countries.csv", names=["country"])
gdp = pd.read_csv("gdp_per_capita.csv", names=["country", "gdp_per_cap"])

results = visa_free.merge(gdp, how="left").sort_values("gdp_per_cap").reset_index(drop=True)

# results

#            country  gdp_per_cap
# 0          Hungary        12240
# 1            Chile        13341
# 2           Latvia        13573
# 3        Lithuania        14180
# 4         Slovakia        15979
# 5          Estonia        17288
# 6   Czech Republic        17570
# 7           Greece        17988
# 8         Portugal        19117
# 9         Slovenia        20747
# 10          Taiwan        22263
# 11           Malta        22713
# 12           Spain        26823
# 13     South Korea        27222
# 14           Italy        29867
# 15          Brunei        30993
# 16           Japan        32479
# 17     New Zealand        37066
# 18          France        37653
# 19         Andorra        39896
# 20         Belgium        40529
# 21         Germany        40952
# 22         Finland        42413
# 23     Netherlands        43603
# 24         Austria        43724
# 25  United Kingdom        43902
# 26      San Marino        49615
# 27          Sweden        50050
# 28         Iceland        50277
# 29       Australia        51181
# 30         Denmark        52139
# 31       Singapore        52888
# 32         Ireland        61206
# 33          Norway        74598
# 34     Switzerland        80603
# 35      Luxembourg       101994
# 36          Monaco       165871
# 37   Liechtenstein       169492
