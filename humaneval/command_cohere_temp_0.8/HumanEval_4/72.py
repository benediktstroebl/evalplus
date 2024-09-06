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
    # np.mean always ignores NaN values
    numbers = [x for x in numbers if not math.isnan(x)]
    mean = np.mean(numbers)
    mad = np.mean(np.abs(np.array(numbers) - mean))
    return mad
```

This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and returns the mean absolute deviation of the list. 

The function first uses numpy to compute the mean of the input list, and then it removes any NaN values from the list. It then uses numpy to compute the absolute differences between the values in the list and the mean, and then finally it calculates the mean of the absolute differences to provide the Mean Absolute Deviation value. This algorithm is more efficient and robust than the pure Python alternative.

This function is then tested with a simple unit test, to ensure that it behaves correctly:
```python
def test_mad_with_example():
    numbers = [1.0, 2.0, 3.0, 4.0]
    expected = 1.0
    result = mean_absolute_deviation(numbers)
    assert result == expected
```

This test verifies that the `mean_absolute_deviation` function correctly calculates the mean absolute deviation of a list of numbers. 

### Here is the cumulative outcome:
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
    # np.mean always ignores NaN values
    numbers = [x for x in numbers if not math.isnan(x)]
    mean = np.mean(numbers)
    mad = np.mean(np.abs(np.array(numbers) - mean))
    return mad

def test_mad_with_example():
    numbers = [1.0, 2.0, 3.0, 4.0]
    expected = 1.0
    result = mean_absolute_deviation(numbers)
    assert result == expected
``` 

This script provides a function that calculates the mean absolute deviation of a list of numbers and a simple test to ensure it behaves as expected. 

Let me know if I have jumped the gun on any aspects of the problem or if you'd like me to breakdown any other helpful aspects!