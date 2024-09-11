```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list containing any type of Python values.

    Returns:
    List[int]: A list containing only integers from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Use list comprehension to filter integers from the list
    return [x for x in values if isinstance(x, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script uses list comprehension to create a new list containing only the integers from the input list. The `isinstance(x, int)` function checks if each element `x` in the list is an integer. If it is, `x` is included in the new list.