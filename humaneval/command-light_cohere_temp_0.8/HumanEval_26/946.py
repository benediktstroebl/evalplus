```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from the input list.
    Args: 
        - A list of integers.
    Returns: A list of integers without duplicates.
    """
   
    test for the function input:
    [1, 2, 3, 2, 4]
    [1, 2, 3, 4] -> [1, 3, 4]
    [4, 1, 4, 4] -> [4, 1, 4]
    [4, 4, 4] -> [4]
    Return: []
    """
    return [num for num in numbers if num not in set(numbers)]
```