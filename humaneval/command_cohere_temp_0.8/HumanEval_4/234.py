Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Example usage
input_data = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(input_data))  # Output: 1.0

```

This script defines the `mean_absolute_deviation` function that takes a list of numbers and returns the mean absolute deviation of the numbers in the list. It utilizes NumPy to process the input list and calculate the mean and absolute deviations. 

To verify the functionality, the `pytest` module is included and an example usage is demonstrated with the `input_data`. When executed, it should print the calculated mean absolute deviation of 1.0, matching the expected output. Feel free to adapt and incorporate this solution in your codebase, and if you have further questions or additional problems, please don't hesitate to ask!