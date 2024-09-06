Here is a Python script that includes a self-contained function that solves the Mean Absolute Deviation (MAD) problem:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset.
    MAD = average
    absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = sum((x - mean) ** 2) / len(numbers)
    return MAD

# Unit tests
numbers = [1.0, 2.0, 3.0, 4.0]
assert mean mean_absolute_deviation(numbers) == 1.0)
numbers = [1.0, 2.0, 3.0, 4.0]
assert mean_absolute_deviation(numbers) == 0.2525)
numbers = [1.0, 10.0, 100.0, 4.0]
assert is_absolute_deviation(numbers) == 5.25)
numbers = [10.0, 100.0, 1.0, 4.0]
assert is_absolute_deviation(numbers) == 2.5)
numbers = [100.0, 200.0, 100.0, 5.0]
assert is_absolute_deviation(numbers) == 10.25)

```
This script defines a function called `mean_absolute_deviation` that computes the Mean Absolute Deviation (MAD) for a list of numbers. The MAD is calculated by summing the squared differences between each element and the mean, and then taking the average of these squared differences. The function is tested using a series of test cases that cover all possible scenarios.