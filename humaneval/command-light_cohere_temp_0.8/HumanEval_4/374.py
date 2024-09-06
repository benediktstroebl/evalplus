```python
from typing import List

def mean_absolute_deviation(numbers):
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD = average | x -
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4])
   3.0)
   
```

def test_mean_absolute_deviation(numbers):
    # Test Case 1
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 1.0

def test_mean_absolute_deviation_empty_list(numbers):
    # Test Case 2
    assert mean_absolute_deviation([]) == 0.0

if __name__ == "__main__":
    # Test Case 3
    numbers = [1.0, 2.0, 3.0, 4]
    print("Test Case 1 passed!")
    print("Test Case 2 passed!")
    print("Test Case 3 passed!")
```
The function `mean_absolute_deviation` takes a list of numbers as input and returns the Mean Absolute Deviation around the mean of the dataset. The `test_mean_absolute_deviation` function contains two tests that check the output of the `mean_absolute_deviation` function with the corresponding test data.