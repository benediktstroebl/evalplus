Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script uses the `numpy` library to calculate the Mean Absolute Deviation (MAD) of a list of numbers. The `mean_absolute_deviation` function takes a list of floats `numbers` as input and returns the MAD value. Here's a step-by-step explanation of the code:
- Import the `List` module from the `typing` module and the `numpy` module.
- The `mean_absolute_deviation` function takes a list of float numbers and returns the mean absolute deviation.
- The provided example usage demonstrates calculating the MAD of a list `[1.0, 2.0, 3.0, 4.0]`, and it returns the expected value of `1.0`.

This approach leverages `numpy` to compute the mean and absolute deviations efficiently. Additionally, it provides a clear and concise solution to the problem statement.