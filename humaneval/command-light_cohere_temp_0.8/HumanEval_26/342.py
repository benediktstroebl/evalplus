```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate elements from a list. 
    Returns a particular list of unique elements.

    1. Remove all duplicates by comparing each elements. 
    2. Find all duplicates and duplicates by getting the duplicates in the list, 
    and then compare all the elements to each other. 
    2.1. Check if the former first list in numbers, sorted in ascending order. 
    """
    keep only the certain element from the list and return it.
```
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4] 
``` 
This Python function, `remove_duplicates`, is intended to accept a list of integers and generate a new list containing only the distinct elements from the original list.