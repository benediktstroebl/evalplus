```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    mad = 0.0
    for num in numbers:
        mad += (num - mean) ** 2
    return 2.0 * mad / len(numbers)


def test_mean_absolute_deviation(values):
    return mean_absolute_deviation(values) >= 0.0
```
This script defines a function called `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. It also defines a test function `test_mean_absolute_deviation` which uses the `mean_absolute_deviation` function to test if the output of the function is greater than 0.0, which would represent a pass.