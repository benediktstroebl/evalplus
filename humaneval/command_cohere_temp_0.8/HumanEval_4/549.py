Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Below are some test cases to validate the mean_absolute_deviation function
def test_mean_absolute_deviation_list_normal():
    expected = 1.0
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    assert result == expected

def test_mean_absolute_deviation_list_with_negative_values():
    expected = 3.0
    result = mean_absolute_deviation([1.0, -2.0, 3.0, -4.0])
    assert result == expected

def test_mean_absolute_deviation_list_all_negative():
    expected = sum(np.abs(np.array( [-1.0, -2.0, -3.0, -4.0] ) - np.mean(np.array( [-1.0, -2.0, -3.0, -4.0])))) / 4.0
    result = mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0])
    assert result == expected

def test_mean_absolute_deviation_list_all_positive():
    expected = sum(np.abs(np.array([1.0, 2.0, 3.0, 4.0]) - np.mean(np.array([1.0, 2.0, 3.0, 4.0])))) / 4.0
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    assert result == expected

if __name__ == '__main__':
    pytest.main([''])
```

This script includes the `mean_absolute_deviation` function, and it also contains test cases (`test_mean_absolute_deviation_list_normal`) to validate the function. 

The `pytest.main([''])` function at the end ensures that the tests are run when the script is executed directly. 

You can add more test cases as needed to cover various scenarios, such as lists with negative and positive numbers, lists with only negative or only positive numbers, etc. 

Run the script directly (`python script.py`) to execute the tests and verify that the `mean_absolute_deviation` function behaves as expected. 
If you encounter any difficulties, please inquire; I'll be glad to help!