```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove elements that occur more than once from a list of integers.
   
    Numbers that appear more than once in the list are eliminated, and the function returns a new list with unique values.

    :param> numbers (List[int]): List of integers.
    -> returns: List[int]: List of integers without duplicates.
    """
   
    test case:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```

This Python code defines a function called `remove_duplicates` that removes duplicate elements from a list of integers. The function uses a `set()` data structure to keep track of elements seen before, and then iterates through the input list, eliminating any elements that have already been seen. The code provides an simple test case, and the function successfully removes duplicates.