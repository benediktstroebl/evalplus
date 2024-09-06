Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script utilizes the numpy library to calculate the Mean Absolute Deviation, which provides a robust and efficient solution. The MAD is then returned as a float value.

To adhere to the TDD principle, we should also provide a corresponding test:
```python
def test_mad():
    # Test case with known result
    numbers = [1, 2, 3, 4]
    expected = 1
    result = mean_absolute_deviation(numbers)
    assert result == expected
```
This particular test case checks if the calculated MAD matches the expected value of 1, further validating the correctness of the implementation.