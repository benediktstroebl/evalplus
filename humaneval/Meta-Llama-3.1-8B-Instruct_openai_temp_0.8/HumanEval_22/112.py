Here is the Python script that solves the problem:
```markdown
# Filter Integers from a List
=====================================

This script filters a list of any Python values and returns a new list containing only the integers.

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of values of any type

    Returns:
        List[int]: A list of integers from the input values

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
values = ['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
integers = filter_integers(values)
print(integers)  # Output: [5, 1, 2, 3]
```

This script uses a list comprehension to filter the input list. The `isinstance(value, int)` check determines whether each value is an integer or not. The resulting list of integers is then returned by the function.