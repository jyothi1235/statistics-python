#descriptive statistics
#1)Measure of central tendency:

#Mean
import numpy as np
arr=list(map(int,input().split()))
mean=np.mean(arr)
print("Mean = ",mean)

#Median
import numpy as np
arr=list(map(int,input().split()))
median=np.median(arr)
print("Median = ",median)

#Mode
import scipy.stats as stats
arr=list(map(int,input().split()))
mode=stats.mode(arr)
print("Mode = ",mode)

#2) Measure of variability

#Range
import numpy as np
arr=list(map(int,input().split()))
range_value=np.ptp(arr)
print(range_value)

#Variance
import numpy as np
arr=list(map(int,input().split()))
variance=np.var(arr, ddof=0)   # best choice
print(variance)

#Standard Deviation
import numpy as np
arr=list(map(int,input().split()))
std_dev=np.std(arr,ddof=0)
print(std_dev)

