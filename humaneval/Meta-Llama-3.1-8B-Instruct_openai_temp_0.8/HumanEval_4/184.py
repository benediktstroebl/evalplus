```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation 
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each 
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    :param numbers: A list of floating point numbers
    :return: The mean absolute deviation of the input list
    """
    # Check if input list is empty
    if len(numbers) == 0:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviation from the mean for each number
    deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(deviations) / len(deviations)

    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. The function first calculates the mean of the input list, then calculates the absolute deviation from the mean for each number, and finally calculates the mean of these absolute deviations. The function returns this final value as the MAD. The test case at the end of the script demonstrates the function's usage.