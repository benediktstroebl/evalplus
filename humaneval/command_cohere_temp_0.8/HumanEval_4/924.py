Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_list_of_numbers(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)

    def test_mean_absolute_deviation_with_single_number(self):
        numbers = [5.]
        self.assertEqual(mean_absolute_deviation(numbers), 0.)

if __name__ == '__main__':
    unittest.main()
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of a list of numbers, as described in the problem statement. It also includes a `unittest` module to test the function with different inputs.

The `mean_absolute_deviation` function calculates the absolute deviation of each number in the list from the mean of the numbers, and then returns the average of these absolute deviations. 

The `TestMeanAbsoluteDeviation` class includes three test methods:
- `test_mean_absolute_deviation_with_list_of_numbers`: This tests passes a list of numbers ( `[1., 2., 3., 4.]`), and the expected result (1.0) to verify the function returns the expected output.
- `test_mean_absolute_deviation_with_empty_list`: This tests verifies if the function raises a `ValueError` error when an empty list is passed.
- `test_mean_absolute_deviation_with_single_number`: This tests checks if the function correctly handles a list with a single element ( [5.] ). 

The `unittest.main()` function is invoked to run the tests. 

This code demonstrates how to thoroughly test a statistical metric with various input scenarios. It can serve as a foundation for more elaborate statistical functions and tests. 

You can modify this code to address other statistical problems and validate your code's correctness using Python's robust testing capabilities.  If you'd like more information on testing strategies or the numpy + typing combo, feel free to ask!