```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    return [max(numbers[:i+1]) for i in range(len(numbers))]

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This Python script uses a list comprehension to generate a new list where each element is the maximum of all elements up to that index in the input list. This is a simple and efficient solution with a time complexity of O(n^2) due to the use of the `max` function inside the list comprehension. 

However, we can improve the time complexity to O(n) by keeping track of the current maximum as we iterate over the input list:

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = float('-inf')
    result = []
    
    for num in numbers:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    
    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This version of the function has a time complexity of O(n) because we only need to iterate over the input list once.