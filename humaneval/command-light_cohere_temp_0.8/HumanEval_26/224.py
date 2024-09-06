```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list with unique elements.
    """
    unique elements remains in the list
    """
    return [x for x in numbers if numbers.count(x) <= 1]
```
This function takes a list of integers as input and returns a new list with the unique elements from the input list. It works by using a `count()` method to keep track of the number of occurrences of each element and returns only the elements that occur at most once in the input list.