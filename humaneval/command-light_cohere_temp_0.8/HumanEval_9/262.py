```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    Return the list of maximum elements with their respective positions in the sequence.
    """
    list[max_roll(numbers, 0)[1:]:
    return numbers[1:]

def max_roll(lst: List[int], position: int) -> Tuple[int, int]:
    """
    Find the maximum element at the given position and return its index.
    """
    list of integers"""
    if position == len(lst) - 1:
        return (lst[-1], lst[-1])
    max_val, index = lst[position], lst[position + 1]
    return (max_val, index)

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Expected output: [1, 2, 3, 3, 3, 4, 4]
print(max_roll(numbers, 5))   # Expected output: (4, 5)
```

This solution defines two helper functions: `rolling_max` and `max_roll`, which take a list of integers and the position as input, respectively. Then, these functions find the maximum element at the given position and return its index.