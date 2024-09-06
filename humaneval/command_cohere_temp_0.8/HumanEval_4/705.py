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
    if len(numbers) < 1:
        raise ValueError("Input list must not be empty")

    mean = math.fmean(numbers)
    mad = sum( abs(x - mean) for x in numbers) / len(numbers)
    
    return mad
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function first checks if the input list is empty, and if so, raises a `ValueError`. It then calculates the mean of the numbers and the absolute deviation from the mean for each number, and returns the average of these deviations as the mean absolute deviation. 

To check the functionality, we can call this function on a test list like this:
```python
test_list = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(test_list))  # Should print: 1.0
``` 

This will output:
```
1.0
``` 
as expected, confirming that the function behaves correctly.