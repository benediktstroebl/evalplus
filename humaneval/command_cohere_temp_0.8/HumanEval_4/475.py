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
pytest.assertAlmostEqual(mean_deviation, 1.0)
```
This script defines the `mean_absolute_deviation` function that takes a list of numbers as input and uses NumPy to calculate the mean absolute deviation of the provided list of numbers. Then, it includes a test block that creates a list of test numbers and prints the result of the function accordingly. The `pytest.assertAlmostEqual` is used to check if the output matches the expected result with an approximation within 8 decimal places. 

Note: In order to run this code, NumPy should be installed. You can do it with: `pip install numpy`

Mean Absolute Deviation (MAD) is a measure of the variability of a dataset. It is the average absolute difference between each element and the center point.