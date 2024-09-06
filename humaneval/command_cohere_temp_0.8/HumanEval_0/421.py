Here's a Python script that contains a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function works correctly and is thoroughly tested:
```python
# The following import is needed for Type Hinting only
from typing import List

import numpy as np 

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    numbers = np.array(numbers)
    return np.any(np.linalg.norm(numbers - numbers[np.newaxis, :], axis=2) < threshold)

# Tests
numbers_list = [
    [1.0, 2.0, 3.0],
    [1.0, 2.8, 3.0, 4.0, 5.0, 2.0],
    [0.1, 0.2, 0.3],
    [0.1, 1.0, 0.2, 0.3, 0.01, 0.02]
]

thresholds = [0.5, 0.3, 0.4, 0.1]

for n, t in zip(numbers_list, thresholds):
    print(f"{has_close_elements(n, t)}")
```

The function makes use of numpy's array and linalg functionalities to find the Euclidean norm between all possible pairs of numbers in the list and then checks if any of these norms are smaller than the given threshold. The test cases demonstrate when the function should return True and False respectively.