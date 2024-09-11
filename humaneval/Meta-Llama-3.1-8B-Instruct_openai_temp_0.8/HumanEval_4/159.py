### Calculating Mean Absolute Deviation in Python

Below is a Python script that defines a function to calculate the Mean Absolute Deviation (MAD) of a given list of numbers.

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation of the given list of numbers.
    """
    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as an argument and returns the Mean Absolute Deviation of the dataset. The function first calculates the mean of the dataset by summing all numbers and dividing by the total count. Then, it calculates the absolute deviation of each number from the mean using a list comprehension. Finally, it calculates the mean of these absolute deviations to get the Mean Absolute Deviation. The example usage at the end demonstrates how to call this function with a list of numbers and print the result.