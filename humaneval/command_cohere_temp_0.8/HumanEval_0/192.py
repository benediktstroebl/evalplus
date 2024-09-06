Here's a Python script that contains a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function works correctly and passes the given tests. The code is formatted as a markdown code block:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    numbers.sort()
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] < threshold:
            return True
    return False

# Tests
numbers_list_1 = [1.0, 2.0, 3.0]
threshold_1 = 0.5
test_1 = has_close_elements(numbers_list_1, threshold_1)
assert not test_1

numbers_list_2 = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
threshold_2 = 0.3
test_2 = has_close_elements(numbers_list_2, threshold_2)
assert test_2
```
The function has_close_elements sorts the list and then iterates through the list, checking if the difference between subsequent elements is less than the given threshold. If any such pair is found, it returns True, otherwise, it returns False. The tests assert the function's correctness for both test cases.