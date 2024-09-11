```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing python values of any type.

    Returns:
        List[int]: A list containing only the integer values from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This Python script defines a function `filter_integers` that takes a list of values of any type and returns a new list containing only the integer values from the original list. The function uses a list comprehension and the `isinstance` function to filter the values. The `isinstance` function checks if a value is an instance of a particular class or type, in this case, `int`.