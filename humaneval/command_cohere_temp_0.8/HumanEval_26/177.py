```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script provides a function called `remove_duplicates`, which takes a list of integers as input and returns a list of unique integers from the input list. It removes duplicate entries from the input list, leaving only unique values, and returns the distinct integer values in the order they appeared in the original list.  This function is useful for cleaning up lists of data where duplicate entries need to be removed while retaining the original order.