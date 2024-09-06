```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    """
    take in a list of integers and returns a new list with unique integers
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
```
Do you need assistance with anything else?