```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from a list of integers and return a new list without duplicates.
    """
    numbers_list = list(set(numbers))
    return [num for num in numbers_list if num not in numbers]
```