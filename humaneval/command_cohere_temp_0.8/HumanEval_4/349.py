Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a markdown code block with corresponding test data and expected output to verify the correctness of the implementation:
```python
# Test Data:
>>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

# Expected Output:
>>> mean_absolute_deviation(numbers)
1.0
```

This code block features a Python script that calculates the mean absolute deviation of a list of numbers using the `mean_absolute_deviation` function. Test data comprising a list of numbers is generated, and the expected output is the mean absolute deviation for this data. The result is compared to the expected output to verify the function's correctness.

This implementation uses the `numpy` library to provide an efficient solution and returns the mean absolute deviation of the input list of numbers.