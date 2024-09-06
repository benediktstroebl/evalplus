```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicates from the input list.
    Args:
        numbers (List[int]): A list of integers.
    Returns: list of integers without duplicates.
    """
example usage:
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
This Python code defines a function called `remove_duplicates`, designed to remove duplicate elements from a list of integers. The function takes a input as a list of integers and returns a new list without any duplicate values. It accomplishes this through a process by creating a set called `seen`, which keeps track of the elements that have been encountered so far. Then, for each element in the input list, it checks if the number is already present in the `seen` set. If it's, it is added to the result list and the seen set is updated to remove this number from further consideration. This code ensures that each number in the input list will only be added to the result list once.