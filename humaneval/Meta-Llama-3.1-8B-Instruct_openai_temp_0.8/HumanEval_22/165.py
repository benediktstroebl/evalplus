```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values: A list of any python values.

    Returns:
        A list of integers from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [val for val in values if isinstance(val, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

In this script, the `filter_integers` function uses a list comprehension to create a new list that includes only the integers from the input list. The `isinstance(val, int)` expression checks whether each value in the input list is an integer.