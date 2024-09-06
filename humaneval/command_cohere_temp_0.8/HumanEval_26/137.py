```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    return list(set(numbers))
```

This code defines a function called `remove_duplicates` that takes a list of integers as input. Inside the function, it uses a set to store unique elements, which removes any duplicate occurrences. Then it converts this set back into a list to retain the order of the original input. The function returns this modified list, which contains only the unique elements from the original input list.