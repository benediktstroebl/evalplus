```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any type of Python values.

    Returns:
        List[int]: A list containing only the integer values from the input.

    Example:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Example usage:
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script defines a function `filter_integers` that takes a list of any Python values, filters out non-integer values, and returns a new list containing only the integer values. The function uses a list comprehension with the `isinstance` function to check if each value in the input list is an integer. The example usage at the end demonstrates how to use the `filter_integers` function with different input lists.