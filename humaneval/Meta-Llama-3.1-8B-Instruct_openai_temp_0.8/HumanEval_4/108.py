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
        numbers (List[float]): A list of floating point numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    if not numbers:  # Check if the list is empty
        return 0.0  # Return 0.0 if the list is empty

    mean_of_numbers = statistics.mean(numbers)  # Calculate the mean of the list
    absolute_deviations = [abs(num - mean_of_numbers) for num in numbers]  # Calculate absolute deviations
    mad = statistics.mean(absolute_deviations)  # Calculate the Mean Absolute Deviation

    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

In this script, we first check if the input list is empty. If it is, we return 0.0 as the Mean Absolute Deviation. Then we calculate the mean of the list using the `statistics.mean()` function. After that, we calculate the absolute deviations from the mean using a list comprehension. Finally, we calculate the Mean Absolute Deviation by taking the mean of these absolute deviations.