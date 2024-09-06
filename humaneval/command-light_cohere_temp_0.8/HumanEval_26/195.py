```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate elements from the input list.
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
```  This Python function called `remove_duplicates` takes a list of integers as input and removes all the duplicate elements from the list, it utilizes a `set` to keep track of the elements that have been seen before and then iterates through the input list, it adds the element to the `set` if it hasn't been seen before, and adds it to the `result` list.