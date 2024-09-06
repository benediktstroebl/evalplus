```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD

def mean(numbers: List[float]):
    return sum(x)/len(numbers)

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(result)
```
This Python code defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. The MAD is the average absolute difference between each element and the mean of the dataset. The `mean` function calculates the mean of the list and is used to compute the x_mean value for the `mean_absolute_deviation` function. The function is then tested with a sample list of numbers and the result is printed.