```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Using Python 3's 'Generalized Sequence' method for 'rolling window'
    return [num for num in numbers if num > max_window[-(len(max_window) - 1) :]]

# List test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
max_result = rolling_max(numbers)
print("List Test:", max_result)

numbers = [1, 2, 3, 7, 4, 3, 2]
max_result = rolling_max(numbers)
print("List Test 2:", max_result)

numbers = [1, 2, 3, 6, 7, 3, 2]
max_result = rolling_max(numbers)
print("List Test 3:", max_result)

numbers = [1, 2, 3, 2, 3, 4, 5]
max_result = rolling_max(numbers)
print("List Test 4:", max_result)
```
The function 'rolling_max' generates a list of rolling maximum elements from a given list of integers. The output of this code block is the list test results.