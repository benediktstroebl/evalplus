Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
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

    def test_mean_absolute_deviation_with_list_of_strings(self):
        values = ['apple', 'banana', 'cherry', 'date']
        with self.assertRaises(TypeError):
            mean_absolute_deviation(values)

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `mean_absolute_deviation()` function calculates the Mean Absolute Deviation of a list of numbers, using the `numpy` library to operate on the input list to calculate the mean and absolute deviations. 

The `TestMeanAbsoluteDeviation` class tests the above function with two cases:
1. Testing on a list of numbers: this tests the function with a list of numbers and expects the result to be close to the known answer (`1.0` in this case). 
2. Testing on a list of strings: this tests the function with a list of strings and expects it to raise a `TypeError` as the function expects a list of numbers. 

The `if __name__ == '__main__'` block runs the tests in the module if the script is run directly. 

To run this script, ensure you have the `numpy` library installed:
```
pip install numpy
``` 
This will execute the `unittest` classes and output whether the tests pass or fail. Hoping this assists in solving your problem! Let me know if you have any questions or if you'd like me to explain any part of the code in detail.