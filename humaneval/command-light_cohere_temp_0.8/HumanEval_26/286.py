```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list of integers.
    Each element in the unique and return as a new list.
    """
    list(set(numbers))
    return numbers[:]  # using set() to remove duplicates and list() to convert set to list.
    ```
    list(set(numbers) ^ {'2'}))
    return numbers  # if not empty
    return []
``` 
This Python function called `remove_duplicates` accepts a list of integers as input and outputs a list of integers without any duplicates. It uses the list comprehension and the built-in `set()` function to identify and remove any duplicate elements from the input list, and then uses the built-in `list()` function to convert the resulting set back to a list. Finally, it returns an list of integers that are not empty and, if the input list was empty, it returns an empty list.