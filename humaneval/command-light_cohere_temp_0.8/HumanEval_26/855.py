```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list with unique integers.
    """
    list comprehension with set is used to filter out duplicates.
    """ Numbers that are duplicates are removed from the list.
    """
    list is returned with the unique elements.
    """ 
input numbers are: [1, 2, 3, 2, 4]
    output: [1, 3, 4]
    """
    return [x for x in set(numbers) if x not in numbers]
```