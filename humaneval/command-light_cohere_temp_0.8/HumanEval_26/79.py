```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from a list of integers and return a new list.
    """
    set(numbers) does not remove duplicates, so we use the unique method 
    from the set module to get a list of unique numbers.
    return list(set(numbers))
    """
    return list(set(numbers))
```

This function takes a list of integers as input and returns a new list that contains only the unique elements from the original list. It utilizes the unique method from the set module in Python, which automatically removes duplicates and returns a list of unique elements. The function then converts this set to a list using the list() constructor and returns the result, which is a list of unique integers. This self- content function can a complete solution to the problem.