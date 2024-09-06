Here is a Python script with a self-contained function that solves the problem of calculating the mean absolute deviation of a list of numbers and passes corresponding tests:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

@pytest.mark.parametrize('test_input, expected', [
     ([1, 2, 3, 4], 1.0),
     ([-1, -2, 3, -4], 2.0),
     ([10, 11, 12, 13], 1.0),
])
def test_mean_absolute_deviation(test_input: List[float], expected: float):
    actual = mean_absolute_deviation(test_input)
    assert actual == expected
```

This script utilizes the `numpy` library to provide an efficient implementation and then provides a test suite with a pytest test that checks a variety of inputs to ensure the correctness of the `mean_absolute_deviation` function. 

To illustrate how to utilize this function, you can invoke it through its filename like so:
```python
import json
with open('mean_absolute_deviation.py', 'rb')::
```
You can add an additional dependency on the `pytest` library to enhance the testing functionality and provide a more comprehensive test suite, which is a common practice in the industry.