```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of python values

    Returns:
        List[int]: A list of integers from the given list

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

This script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integers from the original list. It uses a list comprehension to iterate over the input list and checks each value using the `isinstance` function to see if it is an integer. If it is, the value is included in the output list. The script also includes docstrings and example usage to illustrate how the function works.