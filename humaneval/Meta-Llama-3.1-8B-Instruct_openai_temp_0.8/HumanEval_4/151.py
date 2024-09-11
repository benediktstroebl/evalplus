```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(deviations)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```

In this script, the `mean_absolute_deviation` function calculates the mean of the input numbers using the `statistics.mean` function from Python's standard library. It then calculates the absolute deviation from the mean for each number by subtracting the mean from each number and taking the absolute value. The mean of these absolute deviations is then calculated using `statistics.mean` again. The function returns this mean absolute deviation. The script includes a test case at the end to demonstrate the function's usage.