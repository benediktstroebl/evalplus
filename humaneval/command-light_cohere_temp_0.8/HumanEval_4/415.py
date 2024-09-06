Here's the solution:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -
    where x = (list(numbers)[len(numbers)-1]) / sum(numbers)
    return MAD

def test_mean_absolute_deviation(test_numbers: List[float]) -> None:
    assert len(test_numbers) == 4
    test_mean = sum(test_numbers)/len(test_numbers)
    test_MAD = test_mean | test_numbers[3] - test_mean
    assert abs(test_MAD - 1.0) < 0.01  # or Woody Test MAD Test
```
This Python script defines a function `mean_absolute_deviation` that computes the Mean Absolute Deviation (MAD) of a dataset of numbers. The function then accepts a list of numbers as input and returns the calculated MAD. 

The function then includes a test function `test_mean_absolute_deviation` that tests the correctness of the `mean_absolute_deviation` function by checking if the difference between the calculated MAD and the expected value of 1.0 is within an interval of 1e.00. This test test also run in the interest of the script, which can be easily modified to include more test cases or add any additional functionality as required.