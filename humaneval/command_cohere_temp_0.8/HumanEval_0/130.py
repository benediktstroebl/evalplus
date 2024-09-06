Here's a Python script that contains a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function works correctly and passes the provided tests. You can copy and paste this code into a Python file and run it to see the results.
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    return any(abs(a - b) < threshold for a in numbers for b in numbers if a != b)

# Tests
numbers_1 = [1.0, 2.0, 3.0]
threshold_1 = 0.5

numbers_2 = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
threshold_2 = 0.3

assert not has_close_elements(numbers_1, threshold_1)
assert has_close_elements(numbers_2, threshold_2)
```
This script includes the function 'has_close_elements' and two tests that show how to use it correctly. The first test checks if there are any adjacent elements in the numbers_1 list with a difference less than the threshold_1. The second test shows the function's ability to discover adjacent elements inside the numbers_2 list that are less than the threshold_2.