```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list containing any type of values

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
```
This script uses list comprehension and the `isinstance()` function to filter the input list. It returns a new list containing only the integers from the input list. The function is also documented with a docstring that provides information about its usage, arguments, return value, and examples.