Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import unittest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_single_number(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0)

    def test_mean_absolute_deviation_list_of_two_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0]), 1.0)

    def test_mean_absolute_deviation_list_of_three_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0]), 1.0)

    def test_mean_absolute_deviation_list_of_four_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()
```

Let's break down the code step by step:
- Importing Modules:
   - `from typing import List`: This imports the `List` type from the `typing` module. It ensures that the `numbers` parameter in the `mean_absolute_deviation` function is explicitly declared as a list of float values.
   - `import numpy as np`: This imports the NumPy library, specifically renaming it as `np`. NumPy is a library for numerical computations in Python.
- Function to Calculate Mean Absolute Deviation:
   - `def mean_absolute_deviation(numbers: List[float]) -> float:`: This defines a function named `mean_absolute_deviation` that takes a list of float values (`List[float])` as input and returns a single float value, which is the mean absolute deviation.
- NumPy for Computations:
   - `np.abs(np.array(numbers) - np.mean(np.array(numbers))):` Here, NumPy is used to perform efficient numerical operations on the list of numbers.
   - `np.array(numbers)`: This converts the input list into a NumPy array, allowing for faster numerical operations.
   - `np.mean(np.array(numbers))`: This calculates the mean (average) of the NumPy array, representing the centerpoint of the dataset.
   - `np.abs(np.array(numbers) - np.mean(np.array(numbers))):` calculates the absolute difference between each element of the NumPy array and the mean. It then calculates the mean of these absolute differences, which provides the Mean Absolute Deviation. 
- Unit Testing:
   - `Class TestMeanAbsoluteDeviation(unittest.TestCase)`: This defines a test class that inherits from `unittest.TestCase`. It contains several test methods to validate the behavior of the `mean_absolute_deviation` function.
   - `def test_mean_absolute_deviation_single_number(self):`: This is a test method that takes a single number as input and checks if the mean absolute deviation is zero, which it should be if the input is a single number.
   - `def test_mean_absolute_deviation_list