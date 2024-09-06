Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the code and a test to demonstrate its functionality:
```python
# Ensure tests are running within the Python environment
import sys
sys.path.append(".")

from math import mean
from typing import List
from unittest.mock import patch
from unittest import TestCase

from mean_absolute_deviation import mean_absolute_deviation


class TestMeanAbsoluteDeviation(TestCase):
    def test_mean_absolute_deviation(self):
        numbers = [1., 2., 3., 4.]
        with patch('builtins.print') as side_effect:
            mean_absolute_deviation(numbers)
        expected = mean(map(lambda x: abs(x - mean(numbers)), numbers))
        self.assertEqual(side_effect.call_args_list[0][0][0], expected)
```

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    return mean(map(lambda x: abs(x - mean(numbers)), numbers))
```

This Python script defines a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the `map` function to create a new list of absolute differences between each element and the mean of the list, and then calculates the mean of these absolute differences to return the mean absolute deviation. 

The `test_mean_absolute_deviation` function tests the `mean_absolute_deviation` function with a sample list of numbers and ensures that the printed output (via `side_effect.call_args_list[0][0][0]`), which is the mean absolute deviation, is equal to the expected value. 

To run this test, you would need to have the `mean_absolute_deviation.py` file containing the function definition in the same directory as your test file, and ensure that the directory is added to the Python path using the `sys.path.append(".")` line at the beginning of the script.  This setup enables the `from ... import ...` statements to locate the required modules.  If your Python environment does not have these dependencies, you may need to install them within your environment using `pip install unittest mock`.  This way, you can ensure that the function works as expected and is accessible from your test file.  This approach demonstrates how to modularly test separate components of your code while ensuring they function correctly.  If you encounter any issues, make sure you are running your Python environment with the necessary dependencies and that the directory containing the `mean_absolute_deviation.py` file is accessible.  This setup provides a robust foundation for testing other functions or code segments in conjunction with this `mean_absolute_deviation` function.  This separation of concerns and systematic testing approach is integral to writing maintainable, scalable, and robust code suites.  Any modifications to the function can then be tested effectively, promoting an iterative and continually improving development process.  This approach helps ensure that your Python code behaves as expected and reliably performs the desired tasks.  Any