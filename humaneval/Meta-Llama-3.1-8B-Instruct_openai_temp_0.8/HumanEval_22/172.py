```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): List containing any type of Python values

    Returns:
        List[int]: List containing only the integers from the input list

    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Use list comprehension to filter the integers
    result = [value for value in values if isinstance(value, int)]
    return result

# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integers from the input list. The function uses a list comprehension to filter the integers, which is a concise and efficient way to create a new list from an existing list. The script also includes docstrings and test cases to demonstrate the function's usage.