```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of values of any type

    Returns:
        List[int]: A new list containing only integers from the input list

    Example:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Test the function
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

In this script, we use a list comprehension to create a new list that only includes the integers from the input list. The `isinstance(value, int)` expression checks whether each value in the list is an integer. If it is, the value is included in the new list. If not, it is skipped.