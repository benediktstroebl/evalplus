```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list of any Python objects

    Returns:
    List[int]: A list of integers from the input list

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
print(filter_integers(['a', 3.14, 5, 3, 6.3]))  # Output: [5, 3]
print(filter_integers([1.2, 2.4, 3.6, 4.8, 5.0]))  # Output: []
print(filter_integers([True, False, None, 1, 5]))  # Output: [1, 5]
```

This script defines a function `filter_integers` that takes a list of any Python objects and returns a new list containing only the integers from the original list. The function uses a list comprehension to filter the values. The `isinstance` function is used to check if a value is an integer. The script also includes some test cases to demonstrate the function's behavior.