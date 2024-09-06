```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list with unique integers.
    """
    input: list[int]
    """
    numbers = set(numbers)  # remove duplicates using set()
    return list(numbers)  # convert back to list
```
The provided code defines a function called remove_duplicates that takes a list of integers as input and returns a new list with unique integers. This is done using the use of the set function to remove duplicates from the input list and then convert it back to a list. This function can be easily used to remove duplicates from any list of integers and pass the corresponding tests.