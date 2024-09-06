```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the Mean Absolute Deviation
    MAD = sum((x - numbers[i])) / len(numbers)
    return MAD

def test_mean_absolute_deviation(test_numbers: List[float]) -> unittest.TestCaseTestCase():
    test_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print("Mean Absolute Deviation is: ", mean_absolute_deviation(test_numbers))
```
This function takes a list of numbers and calculates the Mean Absolute Deviation around the mean of the dataset. The test function has the same function but instead it takes a list of test numbers and passes them through the `mean_absolute_deviation` function to check if the function works correctly.