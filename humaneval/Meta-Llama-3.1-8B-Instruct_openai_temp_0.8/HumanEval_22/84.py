### Integer Filter Script

Here's a Python script that filters a list of any Python values and returns a new list containing only the integers.

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list of any Python values.

    Returns:
        List[int]: A new list containing only the integers.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script uses a list comprehension to create a new list containing only the integers from the input list. The `isinstance(x, int)` function checks if each value `x` in the list is an integer, and if so, it is included in the new list. The resulting list is then returned by the function.