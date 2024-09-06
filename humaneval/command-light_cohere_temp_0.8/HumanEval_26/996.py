```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """
    Remove all duplicate elements from the input list.
    """
    return [list(set(numbers))
    """
    return [num for num in set(numbers)]

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
```
The provided code defines a function called remove_duplicates, which takes a list of integers as input and returns a new list with duplicate elements removed. This is function uses the multiple sets to ensure unique elements and then backlists these elements into a new list.