```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list of any python values.

    Returns:
        List[int]: A list containing only integers from the input list.

    Example:
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

This script uses a list comprehension to filter the input list and only include values that are instances of the `int` type.