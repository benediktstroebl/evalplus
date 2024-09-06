Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the code and a test to demonstrate its functionality:
```python
# -*- coding: utf-8 -*-
import numpy as np

from math import isnan
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case).

    Parameters:
        numbers (list): List of numbers.

    Returns:
        float: Mean Absolute Deviation.
    """
    
    # Handling empty input
    if not numbers:
        raise ValueError("Input list is empty.")
    
    # Handling invalid inputs
    for num in numbers:
        if isnan(num):
            raise ValueError("Invalid input: Contains NaN.")
    
    # Calculate mean
    mean = np.mean(numbers)
    
    # Calculate absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    return np.mean(absolute_deviations)

# Test Cases
def test_mad():
    # Test case 1: Basic example
    numbers = [1, 2, 3, 4]
    expected = 1
    result = mean_absolute_deviation(numbers)
    assert result == expected
    
    # Test case 2: Empty list
    try:
        mean_absolute_deviation([])
    except ValueError as e:
        assert str(e) == "Input list is empty."
    
    # Test case 3: List with NaN values
    try:
        mean_absolute_deviation([1, 2, np.nan, 4])
    except ValueError as e:
        assert str(e) == "Invalid input: Contains NaN."

if __name__ == "__main__":
    test_mad()
```

Let's break down the code and explain each part:
- The modules **numpy**, **math** and **typing** have been imported into the code.
- The `mean_absolute_deviation()` function takes a list of numbers as input and calculates the mean absolute deviation. It first checks if the input list is empty, raising a **ValueError** if it is, then verifies if any NaN values are present in the list, throwing an exception if they are. Next, it computes the mean of the numbers using `np.mean()` and calculates the absolute deviations from the mean using a list comprehension. Finally, it returns the mean of these absolute deviations using `np.mean()`.
- The `test_mad()` function contains the test cases to validate the `mean_absolute_deviation()` function. It first tests the function with a basic example and compares the result with the expected value, asserts that they are equal. It then handles test cases for edge scenarios: an empty list, and a list with NaN values, these cases should raise a **ValueError**, hence the code uses **try-except** blocks to catch and check these exceptions.
- Then, the `if __name__ == "__main__":` line verifies if the script is run directly and if it is, executes the `test_mad()` function.