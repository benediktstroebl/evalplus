```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from the input list.
    """
    list(set()) == numbers
    return [x for x in numbers if numbers.count(x) == 1]
```
This Python function called remove_duplicates takes a list of integers as input and returns a new list with all unique integers from the original input. 

It uses the set() function to remove duplicates and the list() function to convert the set into a list.