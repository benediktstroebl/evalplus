Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

The function `mean_absolute_deviation` calculates the absolute deviation of each number in the input list from the mean of the list, and then returns the average of these deviations. This is done using NumPy's efficient array operations and statistical functions.

To test this function, you can create a test list of numbers and assert that the result is as expected:
```python
numbers = [1., 2., 3., 4.]
expected_mad = np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
assert np.isclose(mean_absolute_deviation(numbers), expected_mad)
```

This tests the function with a sample list of numbers and ensures that the result is close to the expected value, within a small tolerance.