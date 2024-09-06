```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate elements from a list of integers.
    Returns a unique elements.
    """
    unique elements left as the unique elements in the list
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
This function, `remove_duplicates`, takes a list of integers as input and removes all duplicate elements. It uses the set to keep track of unique elements and then loops through the input list, appending any elements that are not in the set. This results in a unique list of integers. The function then returns this list of integers without any duplicates.