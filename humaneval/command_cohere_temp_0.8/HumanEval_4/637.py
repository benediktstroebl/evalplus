Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test suite to validate its correctness:
```python
# Importing the necessary typing module
from typing import List

# The function to calculate the mean absolute deviation
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Ensure the input list is not empty and all values are floats
    if not numbers or not all(isinstance(num, float) for num in numbers):
        raise ValueError("Input list must be a non-empty list of floats.")
    
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Return the mean of the absolute deviations
    return sum(absolute_deviations) / len(numbers)

# Sample tests to ensure the function behaves as expected
def test_mean_absolute_deviation():
    # Test case 1: Basic input list with sum close to zero
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

    # Test case 2: Input list with equal values
    assert mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]) == 0.0

    # Test case 3: Extreme values
    assert mean_absolute_deviation([0.0, 1.0, 2.0, 3.0, 4.0]) == 1.5

    # Test case 4: Negative values
    assert mean_absolute_deviation([−1.0, −2.0, −3.0, −4.0]) == 1.0

    # Test case 5: Large positive and negative values
    assert mean_absolute_deviation([10.0, −5.0, 2.0, −3.0, 4.0]) == 3.0

# To run the tests separately, use the following code:
# import unittest
# unittest.main(testRunner='xmlrunner.XMLTestRunner')
```

This script includes a function, `mean_absolute_deviation`, designed to calculate the mean absolute deviation of a list of numbers. It's accompanied by a set of tests, defined using the `unittest` framework, to validate its behavior across various scenarios.

To run the tests in isolation, you can use the following code:
```python
# Import the unittest module and the function to be tested
import unittest
from mean_absolute_deviation import mean_absolute_deviation  # Corrected import here

# Run the tests using the unittest framework
unittest.main(testRunner='xmlrunner.XMLTestRunner')
```

This will run all the test cases and generate an `xml` report which can be useful for integrating this test suite with continuous integration platforms.