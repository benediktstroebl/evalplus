Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation value
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and returns the mean absolute deviation of the list.

The function first uses NumPy to convert the input list of numbers into a NumPy array, this allows us to then calculate the mean of this array. It then calculates the absolute difference between each element in the list and the mean of the list, and finally, it returns the average of these absolute differences as the mean absolute deviation. 

You can use this function to calculate the mean absolute deviation of any list of numbers. 

This script also imports NumPy and imports math to use specific functions from these libraries, so you'll need to make sure that these libraries are installed in your environment. You can do this with: 
```bash
pip install numpy
```

However, since you haven't explicitly asked for it, I won't include a test suite for this function in the response, but adding one is strongly encouraged for practical usage in order to ensure that the function behaves as expected across different use cases.