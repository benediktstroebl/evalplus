Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function called `mean_absolute_deviation` that takes a list of floating numbers as input and returns the mean absolute deviation of the numbers in the list. 

The function employs the NumPy library to calculate the mean and absolute deviations in O(n):
- It uses `np.abs(np.array(numbers) - np.mean(np.array(numbers)))` to subtract the mean of the array of numbers from each number in the list, taking absolute values of these deviations.
- Then, it uses `np.mean()` to calculate the mean of these absolute deviations, returning the final result. 

Overall, this is an efficient solution that provides an accurate mean absolute deviation for the given input list of numbers. 
The script does not include any test cases but they can be added to validate the functionality of the code. Here is an example: 
```python
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0, places=1)
    def test_mean_absolute_deviation_with_list_of_length_one(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0.0)
if __name__ == '__main__':
    unittest.main()
```