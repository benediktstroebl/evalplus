```markdown
**Mean Absolute Deviation Calculator**
=====================================

### Overview

This script calculates the Mean Absolute Deviation (MAD) for a given list of numbers.

### Code
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate Mean Absolute Deviation around the mean of the dataset.

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: Mean Absolute Deviation.
    """
    # Calculate the mean of the dataset
    mean = np.mean(numbers)
    
    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = np.mean(absolute_deviations)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

### Explanation

This script first calculates the mean of the input list using NumPy's `mean` function. Then, it calculates the absolute deviations from the mean by iterating over the list and subtracting the mean from each number. Finally, it calculates the mean of these absolute deviations, which is the Mean Absolute Deviation.

### Notes

*   The `numpy` library is used for efficient numerical computations.
*   The `abs` function is used to calculate the absolute value of the deviations.
*   The example usage demonstrates how to call the `mean_absolute_deviation` function with a list of numbers and print the result.