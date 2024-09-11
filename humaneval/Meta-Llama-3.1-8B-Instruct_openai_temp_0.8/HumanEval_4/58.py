### Calculating Mean Absolute Deviation in Python

Here's a Python function that calculates the Mean Absolute Deviation (MAD) of a given list of numbers.

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
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation of the input numbers.
    """
    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the deviations
    mad = statistics.mean(deviations)
    
    return mad

# Example usage:
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0]
    print(mean_absolute_deviation(numbers))  # Output: 1.0
```

In this script, we use the `statistics` module to simplify the calculation of the mean. This approach makes the code more concise and easier to read.

This function takes in a list of numbers, calculates the mean of the numbers, then calculates the absolute deviation of each number from the mean. Finally, it calculates the mean of these deviations, which is the Mean Absolute Deviation.