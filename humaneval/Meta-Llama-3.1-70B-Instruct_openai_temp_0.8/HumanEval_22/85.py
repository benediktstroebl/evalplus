```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values: A list containing any python values.

    Returns:
        A list of integers.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of values as input, filters out non-integer values, and returns a new list containing only the integers. The `isinstance(value, int)` check is used to determine whether a value is an integer or not. The function is then tested with two example inputs.