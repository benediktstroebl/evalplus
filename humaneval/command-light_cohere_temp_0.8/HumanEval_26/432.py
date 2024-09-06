```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate elements from the input list. 
    Parameters: 
    list[int]: List of integers 
    Returns: 
    list[int]: List of integers without duplicates.
    """
    test: 
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4], 
    "Failed test: Duplicate elements not removed."

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```