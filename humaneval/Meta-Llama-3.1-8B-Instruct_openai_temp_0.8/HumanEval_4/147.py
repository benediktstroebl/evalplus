```markdown
### Python Script to Calculate Mean Absolute Deviation
```python
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
        numbers (List[float]): A list of float numbers.
    
    Returns:
        float: The mean absolute deviation of the input numbers.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    
    mean = statistics.mean(numbers)
    absolute_deviations = [abs(num - mean) for num in numbers]
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

### Explanation:
This script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a given list of numbers. It first checks if the input list is not empty to avoid a `ValueError` when calculating the mean. Then, it calculates the mean of the input numbers using the `statistics.mean` function. Next, it calculates the absolute deviation of each number from the mean using a list comprehension. Finally, it calculates the mean of these absolute deviations using the `statistics.mean` function again, which gives the mean absolute deviation. The function returns this value.