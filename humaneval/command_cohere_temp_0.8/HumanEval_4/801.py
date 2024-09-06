Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the numpy library to operate on arrays and perform calculations efficiently. Specifically, it calculates the absolute deviation of each element from the mean, and then finds the average of these absolute deviations, resulting in the mean absolute deviation. This metric is useful for understanding the spread of data around its central tendency, providing a measure of dispersion that is resistant to outliers.