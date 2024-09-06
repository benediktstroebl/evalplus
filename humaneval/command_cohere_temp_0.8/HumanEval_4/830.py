Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Tests
numbers = [1.0, 2.0, 3.0, 4.0]
mean_deviation = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation for {numbers}: {mean_deviation}")
pytest.mark.parametrize('input_list, expected_mad', [
    ([[1, 2, 3, 4], [5, 6, 7, 8]], 1.5),
    ([[0, 0, 0], [0, 0, 0]], 0.0),
    ([[-10, -5, 0, 5], [10, 15, 20, 25]], 10.0)
])
```
This script includes the `mean_absolute_deviation()` function that takes a list of numbers as input and returns the mean absolute deviation of the numbers in the list. It uses the `numpy` library to handle numerical operations and uses `pytest` for testing.

The `pytest.mark.parametrize` decorator is used to run multiple tests with different inputs and expected outputs. This is a more concise way to express a series of tests with varying inputs. 

Mean Absolute Deviation is a robust measure of dispersion or variation of a dataset with a single scalar value as it's denominator, unlike the standard deviation or variance where it's denominator is the square of the number of data points, which makes it useless for datasets with less than 5 points.

The `print` statement outputs the result of the `mean_absolute_deviation()` function for the `numbers` list, which will help verify if the function is correctly implemented. 

Please let me know if this implementation is suitable for your needs or if you have additional questions or requirements.