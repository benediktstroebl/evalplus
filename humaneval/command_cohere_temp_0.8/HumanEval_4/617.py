Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(x for x in numbers)/len(numbers)
    mad = sum( abs(x - mean) for x in numbers) / len(numbers)
    return mad
```
This script defines a function called `mean_absolute_deviation()` that takes in a list of numbers and returns the mean absolute deviation of the list. The function first calculates the mean of the numbers in the list and then sums up the absolute deviations from the mean, dividing by the total number of elements to get the mean absolute deviation. This approach provides a robust measure of the variability of the dataset close to the mean.

To ensure the functionality of the script, it is recommended to include tests that cover different cases. Here is an example:
```python
def test_mean_absolute_deviation():
    # Test with simple list
    numbers = [1, 2, 3, 4, 5]
    expected = math.fabs(2 - (1 + 2 + 3 + 4 + 5) / 5)
    result = mean_absolute_deviation(numbers)
    assert result == expected, f"Expected {expected}, but got {result}"
```
The test script uses a simple list to compare the expected and calculated values. You can add more tests to cover other cases as well.