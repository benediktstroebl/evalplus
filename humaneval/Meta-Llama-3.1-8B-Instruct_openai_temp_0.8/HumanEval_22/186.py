```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list containing any type of python objects.

    Returns:
        List[int]: A list containing only integers from the input list.

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

This Python script defines a function `filter_integers` that takes a list of any Python objects and returns a new list containing only the integers from the original list. It uses a list comprehension to filter the input list and checks each value's type using the `isinstance` function. The script also includes docstrings and examples to demonstrate how to use the function.