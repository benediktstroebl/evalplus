```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list of any python values

    Returns:
    List[int]: A list of integers from the input list

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script uses list comprehension to create a new list containing only the values from the input list that are instances of `int`. The `isinstance` function checks if a value is of a certain type (in this case, `int`).