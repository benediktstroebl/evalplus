```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from a list of integers.
    Input: numbers is a list of integers.
    Duplicate removal is using set (user-defined) keys, e. Read this as: "Each element of the input list is compared to 
    every other element, and duplicates are removed.
    Return: A new list with no duplicates.
    """
    function utilizes the, and sets the keys of the dictionary, to create a set.
    The set-created using the set() function is then converted back to a list, 
    and duplicates are automatically removed.
    """
    return list(set(numbers))
```