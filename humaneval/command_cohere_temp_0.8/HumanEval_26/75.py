```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without duplicates, keeping the order of elements left unchanged.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This Python script defines a function called `remove_duplicates` that takes a list of integers as input. It removes any elements that occur more than once and returns a new list containing only the unique elements, maintaining their original order. This function addresses the problem statement and produces the desired output while being compatible with Python's typing system.