```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculates the rolling maximum element in a list of integers.
    Each element is the maximum of the list, excluding the last element, 
    and adds the new maximum to the result.
    Args:
    numbers: A list of integers
    Returns:
    A list of integers, where the ith element is the rolling maximum 
    (the maximum of the list, excluding the last element) after 
    removing the last element.

```

Here is the test case: 
```python
# Test case for the rolling_max function
numbers = [1, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
assert rolling_max_result == [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 2, 3, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
assert rolling_max_result == [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 3, 2, 4, 3, 5]
rolling_max_result = rolling_max(numbers)
assert rolling_max_result == [1, 3, 3, 4, 3, 5]

numbers = [1, 2, 3, 5, 3, 2]
rolling_max_result = rolling_max(numbers)
assert rolling_max_result == [1, 2, 3, 3, 5, 5]
```