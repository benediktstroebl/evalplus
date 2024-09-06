```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from a list of integers.
    Input: numbers (List[int])
    Output: List[int] without duplicates
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```

The provided code defines a function called `remove_duplicates` that accepts a list of integers as input and returns a new list without any duplicates. The function utilizes a set to keep track of elements that have been encountered before, ensuring that each unique element is stored only once. The function iterates through the input list, and for each element, it checks whether it's already present in the seen set. If it's not, the element is added to both the result list and the set.