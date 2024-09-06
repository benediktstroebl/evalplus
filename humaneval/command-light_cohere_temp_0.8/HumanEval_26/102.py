```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    return [list of non-duplicate values
    """
    # Initialize Set of Seen Values
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
``` 
This code defines a function remove_duplicates that accepts a list of integers and removes all elements that occur more than once in the list, then returns a new list containing only the non-duplicate values.