```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """
    Remove all duplicate elements from the input list, and return the unique elements.
    """
    list of integers without duplicates.
    """
    list of integers that are not duplicated.
    """

Input:
    numbers: List[int]
    Output:
    List[int] containing only the unique integers from the input list
"""
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This function removes duplicate elements from the `numbers` list and returns a new list containing only the unique elements. It uses the set to keep track of elements that have been seen, then iterates through the input list, adding elements to the result list if they are not already in the set. The output list will contain only the unique elements from the input list.