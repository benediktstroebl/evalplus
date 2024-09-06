Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Should print: 1.0
```

This script defines the `mean_absolute_deviation()` function that takes in a list of numbers and returns the mean absolute deviation of the list, which is then printed out as an example. The NumPy library is also imported to handle vectorized operations on the input list and calculate the mean. Overall, the code achieves the goal of calculating the Mean Absolute Deviation of a provided list of numbers. 
If you have more questions or need further assistance, please let me know!