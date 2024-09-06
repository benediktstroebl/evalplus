```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from the input list. 
    """
   
    list of integers, remove all elements that occur more than once.
    Keep only the real as in the input. 
    """
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result
```
This function removes duplicates from a list of integers and returns a new list without duplicates.