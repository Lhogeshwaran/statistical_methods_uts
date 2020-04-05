import scipy.stats
import numpy as np
import pandas as pd
import math
import statmet as sm

#1.1
drying_time = [3.4, 2.5, 4.8, 2.9, 3.6, 2.8, 3.3, 5.6, 3.7, 2.8, 4.4, 4.0, 5.2, 3.0, 4.8]

drying_time_stats = sm.Distance(drying_time)

#a Sample size
drying_time_stats.sample_size
#sample_size = len(ls)
#print(sample_size)

#b Sample mean
drying_time_stats.mean
#sample_mean = np.mean(drying_time)
#print(round(sample_mean, 2))

#c Sample median
sample_median = np.median(ls)
print(sample_median)

#e Trimmed mean 20%
trimmed_mean = scipy.stats.trim_mean(ls, 0.2)
print(round(trimmed_mean, 2))

#1.2
ls = [18.71, 21.41, 20.72, 21.81, 19.29, 22.43, 20.17,
        23.71, 19.44, 20.50, 18.92, 20.33, 23.00, 22.85,
        19.25, 21.77, 22.11, 19.77, 18.04, 21.12]

#a Sample mean and median
print(f'Sample mean: {round(np.mean(ls),2)}\nSample median: {np.median(ls)}')

#b Trimmed mean 10%
print(f'Trimmed mean 10%: {round(scipy.stats.trim_mean(ls, 0.1), 2)}')

#1.3
no_aging = [227, 222, 218, 217, 225, 218, 216, 229, 228, 221]
aging = [219, 214, 215, 211, 209, 218, 203, 204, 201, 205]

no_aging_stats = sm.Distance(no_aging)

print(f'No aging stats:\nSample mean: {no_aging_stats.mean}\nSample variance: {no_aging_stats.var}\nSample standard deviation: {no_aging_stats.sd}')

no_aging_mean = sm.Distance.mean(no_aging)
aging_meam = calc_mean(aging)

#1.9 (1.3)
no_aging = [227, 222, 218, 217, 225, 218, 216, 229, 228, 221]
aging = [219, 214, 215, 211, 209, 218, 203, 204, 201, 205]

print(f'Sample var (no aging): {round(np.var(no_aging, ddof=1), 2)}')
print(f'Sample sd (no aging): {round(np.std(no_aging, ddof=1), 2)}')
print(f'Sample var (aging): {round(np.var(aging, ddof=1), 2)}')
print(f'Sample sd (aging): {round(np.std(aging, ddof=1), 2)}')

#1.13

battery = [123, 116, 122, 110, 192, 126, 125, 111, 118, 117]

print(f'Sample mean: {round(np.mean(battery), 2)}')
print(f'Sample median: {round(np.median(battery), 2)}')

#1.17
smokers = [69.3, 56.0, 22.1, 47.6, 53.2, 48.1, 52.7, 34.4, 60.2, 43.8, 23.2, 13.8]
non_smokers = [28.6, 25.1, 26.4, 34.9, 29.8, 28.4, 38.5, 30.2, 30.6, 31.8, 41.6, 21.1, 36.0, 37.9, 13.9]

print(f'Sample mean smokers: {round(np.mean(smokers), 2)}')
print(f'Sample mean non_smokers: {round(np.mean(non_smokers), 2)}')
print(f'Sample sd (smokers): {round(np.std(smokers, ddof=1), 2)}')
print(f'Sample sd (non_smokers): {round(np.std(non_smokers, ddof=1), 2)}')
