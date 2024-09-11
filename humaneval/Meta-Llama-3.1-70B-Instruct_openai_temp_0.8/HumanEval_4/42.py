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
        numbers: A list of floating point numbers.

    Returns:
        The Mean Absolute Deviation of the input numbers.
    """
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference of each number from the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

Alternatively, you can use NumPy library which provides `mean` function to calculate the mean of the input numbers. Here is how you can modify the above code to use NumPy:

```python
import numpy as np
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers: A list of floating point numbers.

    Returns:
        The Mean Absolute Deviation of the input numbers.
    """
    # Convert the input list to NumPy array
    numbers_array = np.array(numbers)
    
    # Calculate the mean of the input numbers
    mean = np.mean(numbers_array)
    
    # Calculate the absolute difference of each number from the mean
    absolute_diffs = np.abs(numbers_array - mean)
    
    # Calculate the mean of the absolute differences
    mad = np.mean(absolute_diffs)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

Both versions of the code will give the same output. However, if you are working with large datasets, using NumPy library can provide significant speedup.