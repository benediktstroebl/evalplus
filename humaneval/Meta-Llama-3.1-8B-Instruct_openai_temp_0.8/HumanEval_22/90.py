```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list containing various python data types.

    Returns:
    List[int]: A list containing only integers from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script uses a list comprehension to create a new list containing only the integers from the input list. The `isinstance(value, int)` condition checks if a value is an instance of the `int` type and includes it in the new list if true. The example usage at the end demonstrates how to use the `filter_integers` function with different input lists.