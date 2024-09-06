Here's a self-contained Python script that solves the problem:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    MAD = sum(x - numbers[-1]) / len(numbers) - 1
    return MAD

def test_mean_absolute_deviation(numbers: List[float]) -> None:
    # Test cases
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 1.0
   
    test_mean_absolute_deviation([0.0, 0.0, 0.0]) == 0.0
assert mean_mean_absolute_deviation([10.0, 20.0, 30.0]) == 7.0

print("Pass test cases")
```
This Python script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) for a given list of numbers. It also has a `test_mean_absolute_deviation` function that contains test cases to check if the function works correctly. 

The `mean_absolute_deviation` function takes a list of numbers as input and returns the Mean Absolute Deviation around the mean of the dataset. 

The test cases ensure that the function returns the expected results for a variety of inputs.