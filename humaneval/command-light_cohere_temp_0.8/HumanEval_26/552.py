```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate integers from the input list.
    : Returns a all elements that occur more than once in the input list, and keeps the first occurrence.
    """
    list_of integers from which input list, we create a new list called unique_numbers. 
    We use set(numbers) to remove all duplicate elements. 
    We use list(set(numbers)) to get the unique elements, which are the elements that were first in the original list.
    Args: 
        - numbers (List[int]): list of integers. 
    Returns: 
    Returns: 
        list[int]: list of integers with duplicate elements removed. 
    """
    result of the set() function, which returns the unique elements of the original input list. 
```
This code defines a function called `remove_duplicates` that takes a list of integers as input and returns a list of integers with duplicate elements removed. The function uses the unique(numbers) to remove duplicate elements from the list and then returns the unique elements as the result.