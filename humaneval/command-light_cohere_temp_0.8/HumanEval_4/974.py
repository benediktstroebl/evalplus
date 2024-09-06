Here is a Python script that includes a self-contained function with the capability to calculate and demonstrate the Mean Absolute Deviation:
```python
from typing import List

def mean_absolute_deviation(numbers):
    """ 
    For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x - - x_mean |
    """
    return sum((x - mean) ** 2 for x, mean in zip(numbers, mean)) ** 0.5 / len(numbers)

test_mean_absolute_deviation = [
    [1.0, 2.0, 3.0, 4.0],
    test.
    [ [], float, expected_output, 2.0]
```

This function adds the squared deviation of each number from the mean, and then takes the average of these squared deviations. 

The test_mean_absolute_deviation list contains the input values to test against the function, and the expected output is also a float: 2.0.