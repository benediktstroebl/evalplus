### Mean Absolute Deviation Calculation
#### Python Script

```markdown
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation 
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each 
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        float: Mean Absolute Deviation
    """
    # Calculate mean of the input list
    mean_value = statistics.mean(numbers)
    
    # Calculate absolute deviations from the mean
    absolute_deviations = [abs(num - mean_value) for num in numbers]
    
    # Calculate Mean Absolute Deviation
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This code defines a function `mean_absolute_deviation` which takes a list of float numbers as input and returns their Mean Absolute Deviation. It uses the `statistics` module for calculating the mean, which is more efficient and reliable than a manual implementation. The function then calculates the absolute deviations from the mean and uses the `statistics.mean` function again to calculate the Mean Absolute Deviation.