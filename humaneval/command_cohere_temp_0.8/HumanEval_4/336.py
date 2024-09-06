Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if not numbers:
        raise ValueError("Input list of numbers is empty. Unable to compute MAD.")

    mean = math.fmean(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad
```

This script includes the necessary import statement, a docstring to describe the function, and input validation to ensure the input list is not empty.

You can test this function by calling it with a list of numbers and comparing the result with the calculated mean absolute deviation. For example:
```python
test_list = [1.0, 2.0, 3.0, 4.0]
expected_result = 1.0

result = mean_absolute_deviation(test_list)
assert result == expected_result
``` 
This will ensure that the function behaves as expected. 
Please note you'll need to install the `math` module in your environment in order to use the `math.fmean` function for floating point numbers. 
Let me know if you'd like to proceed with another problem or further clarify any aspect of this solution!