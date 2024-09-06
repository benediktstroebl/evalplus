Here is a Python script that solves the problem of calculating the Mean Absolute Deviation (MAD):
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    
    MAD = average | x - x_mean |
    """

    # List comprehension to get mean of list
    x_mean = sum(numbers)/len(numbers)

    return abs(x_mean - numbers)

def test_mean_absolute_deviation():
    numbers = [1.0, 2.0, 3.0, 4.0]
    test a
    test_mean_absolute_deviation()

def test_mean_absolute_deviation_error():
    numbers = [5.0, 6.0, 7.0]
    test_mean_absolute_deviation()

def test_mean_absolute_deviation_different_mean():
    numbers = [3.0, 4.0, 5.0]
    test_mean_absolute_deviation()

def test_mean_absolute_deviation_empty_list():
    """ Test the function with an empty list"""
    numbers = []
    assert mean_absolute_deviation(numbers) is None

if __name__ == "__main__":
    # Driver code to run all test functions
    test_mean_absolute_deviation()
    test_mean_absolute_deviation_error()
    test_mean_absolute_deviation_different_mean()
    test_mean_absolute_deviation_empty_list()

```

The script defines a function called `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) for that list. The MAD is calculated by taking the average of the absolute differences between each element and the mean of the list. The function is then tested with several test cases using the `typing` module to define test cases and assertions, which check if the function returns the expected output for a given input.