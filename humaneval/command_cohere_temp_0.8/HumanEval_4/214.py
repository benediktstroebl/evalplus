Here's a Python script with a self-contained function that solves the problem you've described, along with a separate test module to validate its correctness:
```python
# problem_solver.py

from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
   Returns:
    (float): Mean Absolute Deviation score for the provided numbers
    """
    if not numbers:
        raise ValueError("Input list 'numbers' cannot be empty.")

    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    
    return mad

# Tests
import unittest
import math

def _test_mean_absolute_deviation():
    # Test Case: Single DataPoint
    assert mean_absolute_deviation([1.0]) == 0.0

    # Test Case: Symmetric DataPoint Distribution
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

    # Test Case: Asymmetric DataPoint Distribution
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == 3.0 / 3

    # Test Case: Large dataset
    numbers = [1 for _ in range(1000000)]
    assert math.isclose(mean_absolute_deviation(numbers), 0.0, rel_tol=1e-6)

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        _test_mean_absolute_deviation()

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `mean_absolute_deviation()` function calculates the Mean Absolute Deviation as described in the docstring. The `_test_mean_absolute_deviation()` function contains specific tests for the function, and the `TestMeanAbsoluteDeviation` class asserts the function's behavior against various test cases. 

Note: The `math.isclose()` function is used for approximate numerical equality tests, allowing for slight floating-point differences. 

The `unittest.main()` call executes the tests when the script is run directly. 

This way, the code is fully self-contained and can be executed independently to verify its functionality. 
You can add this script to your Python environment or copy and paste the code into a Python interpreter session to test and verify the function's behavior against the provided test cases.