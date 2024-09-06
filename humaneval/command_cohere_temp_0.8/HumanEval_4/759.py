Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a Markdown code block with corresponding test data and expected outputs:
```python
import numpy as np
import pytest

def test_mad():
    """Test Mean Absolute Deviation calculation."""
    dataset = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    expected = 1.0
    result = yield_computed_result(mean_absolute_deviation, dataset)
    assert result == expected
```

This script defines a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers. It uses the `numpy` library to operate on arrays and compute the mean and absolute deviations.

The `test_mad` function verifies the calculation against expected results, asserting the output of the function with the expected mean absolute deviation of the provided dataset.