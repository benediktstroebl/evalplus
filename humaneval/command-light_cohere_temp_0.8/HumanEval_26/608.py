```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Removes duplicates from a list of integers.
    Retains only first occurrences of elements, and removes all others.
    """
    list of integers is taken as input
    """
    result = [x for x in numbers if numbers.count(x) == 1]
    return result
```