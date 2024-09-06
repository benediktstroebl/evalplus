```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate elements from a list of integers. 
    Returns a the unique elements as a new list.
    """
   
    list of integers without duplicates
    """
    numbers = set(numbers)
    return [num for num in numbers if num not in numbers]
```