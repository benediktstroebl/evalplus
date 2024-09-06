```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation for a given list of numbers. 
    MAD = average | x -x_mean | 
    where x is each element in the list and x_mean is the mean of the dataset.
    return sum(map(abs, zip(numbers, numbers))) / len(numbers)
    """
    return sum(map(lambda x: abs(x - numbers[len(numbers) - 1]), numbers)) / len(numbers)
```
This function returns the mean absolute deviation (MAD) for a list of numbers. It works by calculating the absolute difference between each element and the mean, then taking the average of these differences and dividing by the length of the numbers. The result is then the mean absolute deviation, which is a measure of the dispersion or spread of data points about the mean.