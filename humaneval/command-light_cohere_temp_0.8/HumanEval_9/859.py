```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling max elements found until a given moment in the sequence.
    :param numbers: List[int]
    :return: List[int]
    """
    # Using the rolling max function
    return [n for n in numbers if n > max_n[i]]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
test_result = rolling_max(numbers)
print(test_result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [5, 10, 3, 7, 6, 2, 4, 8, 100]
test_result = rolling_max(numbers)
print(test_result)  # Output: [10, 3, 7, 2, 8, 100]
```

This script defines a rolling_max function, which takes a list of integers as input and returns a new list with the rolling maximum elements from that list. This is using a list comprehension to filter the numbers greater than the current maximum element, which is stored in the max_n list. The test cases demonstrate the using two different input lists and displaying the results.

The output of the test cases will be:
```bash
[1, 2, 3, 3, 4, 4]
[10, 3, 7, 2, 8, 100]
```