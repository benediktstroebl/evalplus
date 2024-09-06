```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -
        x_mean)
    where x is each element in the list and x_mean is the mean of the list.

def test_mean_absolute_deviation(numbers):
    expected_result = float(1e-5)
    actual_result = mean_absolute_deviation(numbers)
    assert actual_result == expected_result, "Test failed.

numbers = [1.0, 2.0, 3.0, 4.0]
test_mean_absolute_deviation(numbers)
print(test_mean_absolute_deviation(numbers)))
``` 
The provided Python code defines a function called `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) for a given list of numbers. It also has a `test_mean_absolute_deviation` function that takes a list of numbers as input and compares the calculated MAD with the expected value (1e-5) to pass the test.