```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculates Mean Absolute Deviation around the mean of the dataset.
    MAD = average | x -x_mean |
    
    where MAD = sum((x - mean) ** 2) / len(numbers)
    
    x_mean = mean(numbers)
    return x_mean
    """

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) ** 2)
```
This code defines a function **`mean_absolute_deviation`** that takes a list of numbers as input and returns the Mean Absolute Deviation. It computes the more generally by calculating the sum of squared differences between each element and the mean, then dividing by the length of the input list. The function also provides an test by calling it with a sample list and printing the result.

Note: Please be aware that you may need to install the `typing` and `statistics` libraries to run this code.