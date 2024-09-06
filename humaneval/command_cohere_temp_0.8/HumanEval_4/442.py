Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This script utilizes the numpy library, which provides a powerful array structure for numerical operations. The `mean_absolute_deviation` function takes a list of numbers as input and returns the mean absolute deviation, which is the average absolute difference between each element and the mean of the dataset. To calculate the mean, the provided list is converted into a numpy array, and the absolute differences are computed using numpy's subtraction and absolute value functions. The resulting absolute deviations are then returned as the final output.