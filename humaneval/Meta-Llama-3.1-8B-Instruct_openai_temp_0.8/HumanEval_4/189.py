**Mean Absolute Deviation Calculator**
=====================================

Below is a Python script that calculates the Mean Absolute Deviation (MAD) around the mean of a given dataset.

```markdown
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: A list of float numbers
    :return: The Mean Absolute Deviation of the input list
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of float numbers as input and returns the Mean Absolute Deviation (MAD) around the mean of the dataset. It first checks if the input list is empty, raises a `ValueError` if it is, and then calculates the mean of the input list. It then calculates the absolute deviations from the mean using a list comprehension and finally calculates the mean of these absolute deviations, which is the Mean Absolute Deviation.