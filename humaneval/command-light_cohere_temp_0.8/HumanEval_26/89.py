Here is a Python script with a self-contained function that solves the problem of removing duplicates from a list of integers:
```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Remove duplicates from a list of integers.
    # Remove duplicates by setting corresponding elements to None.
    return [set values from the set() and converting to a list of ints
    """
    return [x for x in set(numbers) if x not in numbers]
``` 
This function utilizes the `set()` function and the `not in` operator to identify and remove duplicate elements from the input list. 

The resulting list contains only the unique elements, satisfying the problem's requirement.