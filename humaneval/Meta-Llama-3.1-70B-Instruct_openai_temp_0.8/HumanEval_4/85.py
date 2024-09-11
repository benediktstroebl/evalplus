```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # First, calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)
    
    # Then, calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Finally, calculate the mean of these absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation of {numbers}: {mad}")
```

This script first calculates the mean of the input list. It then calculates the absolute difference between each number in the list and the mean, and finally calculates the mean of these absolute deviations, which is the Mean Absolute Deviation. The result is printed to the console.