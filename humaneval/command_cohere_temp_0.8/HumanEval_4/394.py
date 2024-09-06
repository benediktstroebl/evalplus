Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
The function `mean_absolute_deviation` calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to operate on the input list and calculate the deviation. Firstly, it converts the input list into a numpy array for easier mathematical operations. It then calculates the mean of the array and subtracts it from each number in the array to get the deviation, which is followed by calculating the absolute value of each deviation to ensure the result is positive. Finally, it calculates the mean of these absolute deviations to provide the mean absolute deviation of the provided list. 
The MAD measures the variability of a dataset relative to its mean and is considered a robust statistical measure, as it is not sensitive to outliers as much as the standard deviation is.