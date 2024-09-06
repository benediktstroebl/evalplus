Here's a self-contained Python script that defines a function `remove_duplicates()` to solve the problem of removing duplicate values from an input list of integers and passing the result through tests:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicates from the list of integers.
   
    Remove duplicates by checking if each element is in the set of elements 
    that have already been seen. 
    """ If unique elements using the same in the input list
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   
    return result
```

The function utilizes a set to track unique elements, ensuring each number in the input list is only added to the set once. This prevents duplicates and provides a list with all unique integers.