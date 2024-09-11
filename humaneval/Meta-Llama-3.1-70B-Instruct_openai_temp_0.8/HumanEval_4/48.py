**Mean Absolute Deviation Calculator**
======================================

### Overview

This script calculates the Mean Absolute Deviation (MAD) of a given list of numbers. MAD is a measure of the average distance between each data point and the mean of the dataset.

### Code

```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of the input dataset.

    Args:
    numbers (List[float]): A list of floating-point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input dataset.
    """
    # Calculate the mean of the input dataset
    mean = statistics.mean(numbers)

    # Calculate the absolute differences between each element and the mean
    absolute_differences = [abs(x - mean) for x in numbers]

    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_differences)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation is: {mad}")
```

### Explanation

1. The `mean_absolute_deviation` function takes a list of floating-point numbers as input.
2. It calculates the mean of the input dataset using the `statistics.mean` function.
3. It calculates the absolute differences between each element and the mean using a list comprehension.
4. It calculates the mean of the absolute differences using the `statistics.mean` function again.
5. The result is returned as the Mean Absolute Deviation.

### Example Use Case

In the example usage, we calculate the Mean Absolute Deviation of the numbers `[1.0, 2.0, 3.0, 4.0]`. The output should be `1.0`, which is the expected result based on the definition of MAD.