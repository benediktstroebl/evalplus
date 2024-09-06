Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a markdown code block with corresponding test code:
```python
import unittest
import numpy as np

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        numbers = [1., 2., 3., 4.]
        self.assertEqual(mean_absolute_deviation(numbers), 1.0)

        numbers = [4., 4., 5., 7.]
        mean = np.mean(np.array(numbers))
        deviates = np.abs(np.array(numbers) - mean)
        self.assertEqual(mean_absolute_deviation(numbers), np.mean(deviates))

    def test_mean_absolute_deviation_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `mean_absolute_deviation` function calculates the Mean Absolute Deviation of a list of numbers. It does this by subtracting the mean of the input list from each number, taking the absolute value, and then calculating the mean of these absolute differences using the `numpy` library. 

The test code includes two test functions. `test_mean_absolute_deviation` checks the correctness of the mean absolute deviation calculation by comparing it with manually computed values for specific input lists. `test_mean_absolute_deviation_empty_list` ensures that the function raises a `ValueError` when an empty list is passed, confirming the expected behavior. 

To run the test, copy this code into a Python file and execute the file. The `unittest` framework will run the test functions and report on whether the functions pass or fail.