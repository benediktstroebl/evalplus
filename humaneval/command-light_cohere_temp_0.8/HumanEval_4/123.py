Here's the code to solve the problem:
```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x is the list of numbers and x_mean is the mean of the list.
    # Test case:
    assert(isinstance(numbers, List[float]))
    assert(numbers and len(numbers) > 0)
    assert(isinstance(mean(numbers), float))
    assert(abs(mean(numbers) - numbers[0]) < MAD)
    assert(abs(numbers[-1] - mean(numbers)) < MAD)
    return MAD
```
This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation of the list. The function uses the validation to ensure the input is a list of floats, that the list is not empty, and that the mean of the list is a float.