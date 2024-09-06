```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling max elements from a given list of integers.
    Return a max elements, with the order of elements in the list.
    """
    time is like a list comprehension approach, where we iterate through the list and find the maximum element within each rolling window of size 1 (i.

"""
    rolling_max_list = [max(numbers[:i + 1]) for i in range(len(numbers)))]
    return rolling_max_list

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 3, 4, 2]
    print("Rolling Max:", rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers. The function uses a list comprehension approach to achieve this, where it iterates through the input list and finds the maximum element within each rolling window of size 1. The output of this script is a list of numbers where the maximum elements are in order.