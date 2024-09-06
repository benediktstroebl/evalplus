```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Removes duplicate elements from the input list and returns the result.
    """
    list comprehension, using the set() function, removes all duplicate elements and returns the unique elements.
    """
   
    set(numbers)
    return list(numbers)
```