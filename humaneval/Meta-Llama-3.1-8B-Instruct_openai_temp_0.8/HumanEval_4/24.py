```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers: A list of float numbers.

    Returns:
        The Mean Absolute Deviation of the input numbers.
    """
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(deviations) / len(deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

### Explanation

This script defines a function `mean_absolute_deviation` that takes a list of float numbers as input and returns their Mean Absolute Deviation. The function first calculates the mean of the input numbers, then calculates the absolute deviations from the mean, and finally returns the average of these deviations.

### Step-by-Step Breakdown

1.  Calculate the mean of the input numbers using the formula `sum(numbers) / len(numbers)`.
2.  Calculate the absolute deviations from the mean by subtracting the mean from each number and taking the absolute value.
3.  Calculate the Mean Absolute Deviation by averaging the absolute deviations.

### Time Complexity

The time complexity of this script is O(n), where n is the length of the input list, because it involves a single pass through the list to calculate the mean and absolute deviations.