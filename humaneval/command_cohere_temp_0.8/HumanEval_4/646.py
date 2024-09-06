Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Below are some test cases to catch basic errors and ensure edge cases behavior matches expected behavior.

def test_empty_input():
    with pytest.raises(ValueError):
        mean_absolute_deviation([])

def test_single_number():
    assert mean_absolute_deviation([1.0]) == 0.0

def test_array_of_two():
    assert mean_absolute_deviation([1.0, 2.0]) == 1.0

def test_large_dataset():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    assert mean_absolute_deviation(numbers) == 1.0
```

This script includes the `mean_absolute_deviation` function, which calculates the mean absolute deviation of a list of numbers, as well as test cases to check for invalid inputs and ensure the function's behavior matches the expected behavior for various input scenarios. 

Let's break down the code:
1.  `import numpy as np`: This line imports the NumPy library, which provides numerical operations.
2.  `from typing import List`: This line imports the `List` module from the `typing` module. It's used to annotate variable types in Python 3.
3.  `def mean_absolute_deviation(numbers: List[float]) -> float`: This is the definition of the `mean_absolute_deviation` function. It takes a list of float numbers (`List[float])` and returns the mean absolute deviation of the list.
4.  `return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))`: This line is where the main calculation happens. It converts the input list into a NumPy array, calculates the mean of the array, and then calculates the absolute difference between each element and the mean. It then returns the mean of these absolute differences, which is the Mean Absolute Deviation.
5.  `test_empty_input()`: This function tests the behavior of `mean_absolute_deviation()` with an empty list as input. It uses the `pytest.raises` context manager to ensure that a `ValueError` is raised when an empty list is passed.
6.  `test_single_number()`: This function tests the function with a list containing a single number. It asserts that the mean absolute deviation of a single number is 0.
7.  `test_array_of_two()`: This function tests the function with a list containing two numbers. It asserts that the mean absolute deviation of such a list is 1.
8.  `test_large_dataset()`: This function tests the function with a list of ten numbers. It asserts that the mean absolute deviation for this list is 1.0.

You can add more test cases as needed, depending on the specific use cases and requirements you have for the `mean_absolute_deviation` function.