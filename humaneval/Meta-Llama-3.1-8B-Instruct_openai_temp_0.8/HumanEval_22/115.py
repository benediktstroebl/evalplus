```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list of any python objects.

    Returns:
    List[int]: A list of integers from the input.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This Python script implements the `filter_integers` function, which takes a list of any Python values and returns a new list containing only the integers from the original list. The function uses a list comprehension to filter out non-integer values. The `isinstance(value, int)` function checks whether a value is an instance of the `int` type.