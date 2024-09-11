```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a given list of numbers.
    
    The MAD is the average absolute difference between each element and the mean of the dataset.
    
    Args:
        numbers: A list of floating point numbers.
    
    Returns:
        The Mean Absolute Deviation of the input list.
    """
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation is: {mad}")
```

When you run this script, it will calculate the Mean Absolute Deviation of the list `[1.0, 2.0, 3.0, 4.0]` and print the result. You can replace this list with any other list of numbers to calculate their MAD.

Alternatively, you can use the `numpy` library to simplify the calculation:

```python
import numpy as np
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(numbers)))


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation is: {mad}")
```

This version of the function uses `numpy` to calculate the mean and absolute deviations in a more concise way.