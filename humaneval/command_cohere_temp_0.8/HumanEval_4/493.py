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
    if len(numbers) == 0:
        return 0.0  # Return 0 if the input list is empty
    mean = math.fmean(numbers)  # Calculate the mean of the list
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)  # Calculate sum of absolute deviations
    return mad
```

This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. The function first checks if the input list is empty, in which case it returns 0. It then calculates the mean of the numbers and the sum of absolute deviations from the mean, using a list comprehension, and divides the sum by the number of elements to obtain the mean absolute deviation. 

Here's an example of how you can use the function:
```python
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

This will output:
```
1.0
```

This corresponds to the example provided earlier. 

This script provides an implementation of the mean absolute deviation calculation that aligns with the problem statement and should yield the correct result for a list of numbers.  If you have additional questions or need further assistance, feel free to ask!