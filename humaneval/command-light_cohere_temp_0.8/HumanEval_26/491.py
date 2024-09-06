```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
numbers = [1, 2, 3, 2, 4, 2, 1, 4]
print(remove_duplicates(numbers))  # [1, 2, 3, 4]
```
The provided code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The set() function is used to create a new set from the input list, and the list() function is used to convert the set back into a list.

The function then returns the resulting list with duplicates removed.