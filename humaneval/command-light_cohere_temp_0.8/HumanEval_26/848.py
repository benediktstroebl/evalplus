```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers, returns a new list with unique values.
    Args:
        numbers: list of integers
    Returns:
        list of integers, with duplicates removed
    """
    seen = {}
    result = []
    for num in numbers:
        if num not in seen:
            seen[num] = True
            result.append(num)
    return result
``` 
This Python function, `remove_duplicates`, takes a list of integers as an argument and returns a new list with unique integer values. The function uses a dictionary, `seen`, to keep track of numbers that have already been seen. The function iterates through the unique integers and adds them to the `result` list. The function also ensures that the input list is not modified.