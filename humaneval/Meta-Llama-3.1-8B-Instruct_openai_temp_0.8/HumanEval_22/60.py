```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any python values.

    Returns:
        List[int]: A list of integers from the input list.

    Example:
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

This script uses a list comprehension to create a new list that includes only the integer values from the input list. It does this by iterating over each value in the input list and checking if it is an instance of the `int` type using the `isinstance()` function. If it is, the value is included in the new list; otherwise, it is ignored. The new list is then returned by the function.