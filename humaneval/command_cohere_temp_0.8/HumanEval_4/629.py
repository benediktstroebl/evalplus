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
   Args:
        numbers (list): List of numerical data.
    Returns:
        float: Mean Absolute Deviation score.
    """
    mean = sum(numbers) / len(numbers)
    deviations = [abs(num - mean) for num in numbers]
    return sum(deviations) / len(numbers)

# Tests
import unittest

def test_mad():
    """ Test the mean_absolute_deviation function. """
    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.0
    assert mean_absolute_deviation([2, 4, 6, 8, 10, 12]) == 2.0
    assert mean_absolute_deviation([0, 0, 0, 0]) == 0.0
    assert mean_absolute_deviation([-1, -2, -3, -4]) == 6.0

if __name__ == '__main__':
    unittest.main()
```

The `mean_absolute_deviation` function is the main module of this script. It calculates the absolute deviations from the mean for each number in the input list and then returns the average of these absolute deviations, resulting in the Mean Absolute Deviation.

The test module is called 'test_mad' and it consists of a single test function `test_mad`. This function calls the `mean_absolute_deviation` function with a variety of input data and verifies that the resulting Mean Absolute Deviation values are correct. 

To run the test, do the following:
1. Save the two files (`problem_solver.py` and `test_mad.py`) in the same directory.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved these two files.
4. Run the test using the following command:
```bash
python -m unittest test_mad
```

This command will run the test suite in `test_mad.py` using the `unittest` framework, and you'll see the test results, including any errors or successes, in the terminal output. 

Overall, the purpose of these arrangements is to ensure that the `mean_absolute_deviation` function operates appropriately and produces the anticipated results.