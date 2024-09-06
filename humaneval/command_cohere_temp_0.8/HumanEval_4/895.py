Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a markdown code block with corresponding test data and expected output:
```python
import numpy as np

numbers = [1.0, 2.0, 3.0, 4.0]
expected_mad = 1.0

test_data = [
    [numbers, expected_mad],
]

for numbers, expected_mad in test_data:
    result = mean_absolute_deviation(numbers)
    assert result == expected_mad
```

This script uses the `numpy` library to provide an efficient way to manipulate arrays and perform mathematical operations. The `mean_absolute_deviation` function takes a list of numbers as input and returns the mean absolute deviation of the numbers in the list. 

The test dataset includes a list of test numbers and the corresponding expected mean absolute deviation. The `assert` statement compares the actual mean absolute deviation value against the expected value, ensuring they are equal and thereby verifying the correctness of the implementation.  This code block can be copied and pasted into a Python environment to validate the correctness of the provided function.