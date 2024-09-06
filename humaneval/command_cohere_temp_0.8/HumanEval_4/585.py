Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation
    """
    mean = sum(numbers) / len(numbers)
    mad = sum(math.fabs(x - mean) for x in numbers) / len(numbers)
    return mad
```

The function ``mean_absolute_deviation`` calculates the mean of the input list of numbers, then calculates the absolute deviation of each number from the mean, and finally computes the average of these absolute deviations to provide the Mean Absolute Deviation (MAD) value. 

To ensure due diligence, here's an example usage of the function and its test case:
```python
def test_mad():
    """Test case for mean_absolute_deviation function"""
    numbers = [1.0, 2.0, 3.0, 4.0]
    mad = mean_absolute_deviation(numbers)
    assert mad == 1.0
```

This test case ensures that the mean absolute deviation function is correct and aligns with the problem statement. It confirms that the function returns the correct result for the provided input.

```python
test_mad()
```

Therefore, this complete script now incorporates the function, example usage, and a passing test case. Feel free to use or customize this code as required.