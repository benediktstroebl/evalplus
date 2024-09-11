### Filter Integers from a List
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list containing any type of python values

    Returns:
    List[int]: A list of integers filtered from the input list

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
This script defines a function `filter_integers` that takes a list of any type of python values and returns a new list containing only the integers from the input list. It uses a list comprehension to achieve this, which is a concise way to create lists in Python.

The `isinstance(value, int)` function is used to check if each value in the list is an integer. If it is, the value is included in the new list. Otherwise, it is not.