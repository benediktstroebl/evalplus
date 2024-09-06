```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all elements that occur more than once from a list of integers. 
    Returns a duplicates gone list 
    """
    set(numbers) = set(numbers)
    seen = set()
    return [x for x in numbers if x not in seen and x not in set]
```
The function takes a list of integers as input and returns a new list with all elements that are not in the set of seen elements and not in the set of duplicates.

This function follows the principles of sets to efficiently remove duplicates. It utilizes the unique property of a set, where duplicates are not allowed, and a list comprehension to filter out elements that are not in the set of seen elements.

This function can be used to remove duplicates from any list of integers. The output list is guaranteed to have no duplicate elements.