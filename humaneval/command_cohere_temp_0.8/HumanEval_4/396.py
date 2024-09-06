Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(mean_absolute_deviation([1., 2., 3., 4.]), 1.0)
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.)
    def test_large_deviations(self):
        self.assertEqual(mean_absolute_deviation([5., 10., 15., 20.]), 5.0)

if __name__ == '__main__':
    unittest.main()
```
This script includes a function called `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It utilizes the `numpy` library to operate on arrays, making the calculation more efficient. The function is then tested through a series of tests that cover different scenarios such as empty lists and large deviations. Finally, `unittest.main()` is called to run the tests.  This code is encapsulated and provides a standalone solution to the problem, making it easy to reuse and maintain.  By running the script, you can see the test results and verify that the function behaves as expected.  This approach promotes the concept of testing, making it a good practice in software development.  You can also use this script as a starting point and adapt it to other scenarios or extend it further based on your needs.  Feel free to ask any questions or explore further ideas with code!