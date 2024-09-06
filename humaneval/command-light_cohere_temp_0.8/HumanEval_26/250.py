```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicates from the list of integers.
    :param numbers: List[int]
    :return: List[int]
    """
    return list(set(numbers))
```

This function, named `remove_duplicates`, takes a list of integers `numbers` as input and returns a new list with all distinct integers from the input list. The function utilizes the process to remove duplicates by converting the input list into a set using the `set` function, and then converting the set back into a list using the `list` function. 

This approach guarantees that no duplicate values are present in the output list, effectively solving the problem of removing duplicates from a list of integers.