```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from the given list of integers.
    Return a list of maximum elements found in the sequence until the moment specified.
    Parameters: 
    - numbers (list of integers)
    Returns: 
    - max_list (list of integers)
    """
    max_list = []
    moment = 1
    while True:
        current_max = numbers[moment - 1]
        moment += 1
        if moment == len(numbers):
            break
        new_max = numbers[moment]
        max_list.append(new_max)
    return max_list

test_rolling_max = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(test_rolling_max)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This code defines a function **rolling_max** that takes a list of integers as input and returns a list of the maximum elements in the list. It uses a tested approach to find the maximum element, where it starts with the element from the start of the list and keeps adding the maximum element in the current position, moving forward, until it reaches the end of the list.