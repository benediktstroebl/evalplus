```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD

def mean(numbers: List[float]):
    """ Return the mean of the list of numbers """
    return sum(numbers)/len(numbers)

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
print(f"Mean Absolute Deviation is: {numbers[0] - 4.0}")
```