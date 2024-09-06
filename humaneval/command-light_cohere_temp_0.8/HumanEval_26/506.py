Here is a Python script that includes the `remove_duplicates()` function to solve the problem:

```python
from typing import List

def remove_duplicates(numbers: List[int]):
    """ Removes duplicates from a list of integers, returns a unique list.
    numbers = [1, 2, 3, 2, 4, 1]
    return list(set(numbers))
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a unique list of integers by removing any duplicates. The function uses the `set()` and `list()` to create a unique set of integers from the input list, and then returns a list containing only the elements from that set.

This function is self-contained, which means it does not require any external functions or modules to be called, and it can be used directly within the script or passed to other scripts as a standalone function.