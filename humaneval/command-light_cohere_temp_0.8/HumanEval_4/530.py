```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """ 
    Calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    numbers.append(mean()) 
    return sum(map(lambda x: abs(x - mean),numbers))) / len(numbers)

# Unit Tests
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 1.0)

numbers = [5.0, 1.0, 3.0, 4.0, 7.0]
print(mean_absolute_deviation(numbers) == 1.4)

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.0)

numbers = [0.0, 0.0, 0.0, 5.0]
print(mean_absolute_deviation(numbers) == 0.8)

numbers = [5.0, 5.0, 5.0]
print(mean_absolute_deviation(numbers) == 0.04)

numbers = [1.0, -1.0, -2.0, 3.0]
print(mean_absolute_deviation(numbers) == -0.8)

numbers = [1.0, 2.0, 3.0]
print(mean_absolute_deviation(numbers) == 0.04)

``` This script defines a function mean_absolute_deviation that computes the Mean Absolute Deviation (MAD) for a given list of numbers. The function adds the mean of the dataset to the list, and then returns the sum of the absolute differences of each element from the dataset with respect to the mean.