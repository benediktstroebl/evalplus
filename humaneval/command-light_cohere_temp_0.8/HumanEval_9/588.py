```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements in a given list of integers.
    """
    Returns a list comprehension to filter the elements with
    increasing and decreasing order, then find the maximum element
    """
    return [num for num, _ in zip(numbers, numbers[1:]) if num >= numbers[0]]
``` 
This Python function, rolling_max, takes a list of integers as input and returns a list of the rolling maximum elements found within the sequence. It achieves this by iterating through pairs of elements in the input sequence, comparing each pair, and keeping track of the maximum element found so far. The function utilizes a list comprehension to filter the elements with increasing and decreasing order, and then finds the maximum element within the sequence.