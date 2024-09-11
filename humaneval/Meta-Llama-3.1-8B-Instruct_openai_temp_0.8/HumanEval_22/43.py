```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values: A list of values that can be of any Python type.

    Returns:
        A list of integers from the input list.

    Example:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script uses a list comprehension to create a new list containing only the integers from the input list. The `isinstance(x, int)` function checks if each value `x` is an integer. If it is, then `x` is included in the output list.