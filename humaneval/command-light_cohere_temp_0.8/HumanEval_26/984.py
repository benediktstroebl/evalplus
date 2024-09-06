```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the list, and return a new list with unique values.

    """
    list_set()
    new_list = list(set(numbers))
    return new_list
```
This function utilizes the `set()` function to create a set of unique integers from the input list. Then, it creates a new list using the `list()` function and populates it with the elements from the set. The function effectively removes all duplicates and returns a list with unique integers.

In this implementation, we're using the `List[int]` syntax to define a list of integers. The function then calls `list()` and passes the elements from the `set()` function, resulting in a list with distinct values. The function is effectively removing duplicates and providing a new list with unique elements.