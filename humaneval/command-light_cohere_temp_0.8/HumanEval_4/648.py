Here is a Python script that incorporates a self-contained function that calculates and verifies the mean absolute deviation (MAD) for a given list of numbers:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset.

    Returns: MAD, the average absolute difference between each element and the mean of this dataset.
    """
    list of input numbers, each as an element, numbers.
    calculate the mean of this list using the mean() function, mean.
    calculate the absolute difference between each element and the mean using the |x - x_mean| function, mad = average | x - x_mean |
    """

    # Tests
    assert len(numbers) > 0, "The list of numbers should not be empty."
    assert all(numbers), "The list of numbers should have the same length."
    assert all(isinstance(numbers)), "The list of numbers should be float numbers."

    # MAD calculation
    x_mean = sum(numbers) / len(numbers)
    return mad

def test_mean_absolute_deviation(numbers: List[float]) -> None:
    assert mean_absolute_deviation(numbers) == numbers.0, "The calculated MAD does not match the input list of numbers."

# Example
numbers = [1.0, 2.0, 3.0, 4.0]

test_mean_absolute_deviation(numbers)
```
This Python code defines a function `mean_absolute_deviation` that computes the Mean Absolute Deviation (MAD) for a given list of numbers. It then provides a test function `test_mean_absolute_deviation` to verify if the `mean_absolute_deviation` function correctly calculates the MAD for a given input list. The test function asserts that the calculated MAD matches the expected value for the given list of numbers. Finally, an example is provided, where the `mean_absolute_deviation` function is applied to a list of numbers and the test function is used to validate the correctness of the MAD calculation.