```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns the list of rolling maximum elements in the given list of integers.
    The sequence is a simple sum-based approach with a rolling window.
    Args:
        numbers: list of integers
    Returns:
        list of integers: [max(numbers[0]], max(numbers[1]), ... max(numbers[-2]))] 
    """
    numbers = sorted(numbers) + [0]
    return [x for x in numbers[-len:range(len(numbers) - 1)]]

# Tests
numbers = [3, 2, 1, 4, 5, 6]
result = rolling_max(numbers)
assert list(result) == [5, 4, 3, 6, 3]
print("Result:", result)

numbers = [0, 1, 2, 3, 4, 5]
result = rolling_max(numbers)
assert list(result) == [0, 1, 2, 3, 4]
print("Result:", result)

numbers = [3, 2, 1, 4, 5, 6, 7]
result = rolling_max(numbers)
assert list(result) == [0, 1, 2, 3, 4]
print("Result:", result)
```
The provided Python script defines a function `rolling_max` that calculates the list of rolling maximum elements within a given list of integers. 

It uses a simple sum-based approach with a rolling window to achieve this. The function accepts a list of integers as input and returns a new list containing the rolling maximum elements. The script also includes several tests to validate the correctness of the `rolling_max` function.