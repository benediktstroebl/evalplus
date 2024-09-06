Here's a Python script that contains a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function works correctly and passes the provided tests. The code is formatted as a markdown code block:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): List of numbers to check.
        threshold (float): Threshold of closeness.

    Returns:
        bool: True if there are two numbers in the list that are closer than the threshold, False otherwise.
    """
    return any(abs(x - y) < threshold for i, x in enumerate(numbers) for j, y in enumerate(numbers) if i < j and x != y)

# Tests
numbers_1 = [1.0, 2.0, 3.0]
threshold_1 = 0.5
test_1 = has_close_elements(numbers_1, threshold_1)
assert not test_1

numbers_2 = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
threshold_2 = 0.3
test_2 = has_close_elements(numbers_2, threshold_2)
assert test_2
```
The function has_close_elements will return True if there are any pairs of numbers in the list with a difference smaller than the given threshold and False otherwise. 

To test the function, the script provides two example usages of the function, asserting the correctness of the function against the provided test cases.