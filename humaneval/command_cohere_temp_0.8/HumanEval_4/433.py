Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

The function `mean_absolute_deviation` calculates the mean absolute deviation of the input list of numbers. It utilizes NumPy to perform the computations efficiently. First, it creates a NumPy array from the input list, and then, it computes the mean of the absolute differences between each element and the mean of the array. Finally, it returns the mean absolute deviation as the output.