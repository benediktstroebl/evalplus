```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation. Calculate the average absolute difference between each element and the mean of the dataset.
    x_mean = mean(numbers)
    MAD = sum((x - x_mean) ) / len(numbers)
    return MAD

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 0.25)
numbers = [1.0, 2.0, 3.0, 4]
print(mean_absolute_deviation(numbers)) == 0.25)
numbers = [1.0, 2.0, 3.0, 4]
print(mean_absolute_deviation(numbers)) == 0.25)
numbers = [1.0, 2.0, 1.0]
print(mean_absolute_deviation(numbers)) > 0.25)
```