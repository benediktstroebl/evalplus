```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([5.5, 3, 'abc', 1, 2]))  # Output: [3, 1, 2]
```

In this script, we use a list comprehension to create a new list containing only the integers from the original list. The `isinstance(value, int)` function is used to check if each value is an integer. If it is, the value is included in the new list.