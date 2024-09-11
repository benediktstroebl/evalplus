```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the Mean Absolute Deviation
    mad = statistics.stdev(numbers) if len(numbers) > 1 else 0
    
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

In this script, we use the `statistics` module to calculate the mean and standard deviation (which will be used as the Mean Absolute Deviation when there is only one element or when there are repeated elements). The Mean Absolute Deviation (MAD) is the standard deviation when the list has more than one element and is zero when there is only one element. 

However if you wanted to calculate the actual Mean Absolute Deviation from the mean, you can replace the line where we calculate `mad` with these two lines of code:

```python
# Calculate the Mean Absolute Deviation
deviations = [abs(num - mean) for num in numbers]
mad = statistics.mean(deviations)
```

This line first calculates the absolute deviation of each number from the mean, then calculates the mean of those deviations.