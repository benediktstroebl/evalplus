Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import pytest

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))

# Tests
numbers = [1, 2, 3, 4, 5]
mean_deviation = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation for {numbers}: {mean_deviation}")
pytest.assertAlmostEqual(mean_deviation, 1.0, places=1)
```

This code uses the `numpy` library to provide a more efficient implementation and also includes a test using `pytest`. The test case includes a assert statement to check whether the calculated Mean Absolute Deviation matches the expected output. The `pytest.assertAlmostEqual` function is used to allow for slight floating point deviation during testing. 

To run the test, you can save the code into a Python file (e.g., `test_mean_absolute_deviation.py`) and execute the file using the command `python test_mean_absolute_deviation.py` in your terminal. 

This will run the test and display an error if the test case fails, or produce a more concise output if the test case passes, indicating that the test case has completed successfully.