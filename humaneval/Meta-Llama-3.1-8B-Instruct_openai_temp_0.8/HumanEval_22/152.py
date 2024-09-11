```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list of any python values.

    Returns:
    List[int]: A list of integers from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script uses list comprehension to filter out non-integer values from the input list. The `isinstance` function is used to check if each value is an instance of the `int` type. If it is, the value is included in the output list; otherwise, it is skipped.