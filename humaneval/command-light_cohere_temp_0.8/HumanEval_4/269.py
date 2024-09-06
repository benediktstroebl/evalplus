Here's the solution to the problem:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD = average | x - - each element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
   
1.0)  # 0.7563
  # 
The Mean Absolute Deviation is a measure of the dispersion of data set. 
The MAD is the average absolute difference between each data point and the mean. 
The MAD is less sensitive to outliers than the mean and standard deviation. 
The MAD is easier to calculate than the mean and standard deviation. 
This is a good tool to use for analyzing data sets, especially when you want to find outliers. 
It's also used a lot in data science and statistics to find outliers in a data set.