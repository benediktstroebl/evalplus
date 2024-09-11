```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list containing any type of python values.

    Returns:
    List[int]: A list containing only integers from the input.

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

In this script, the `filter_integers` function uses a list comprehension to iterate over the input list. It checks each value using the `isinstance` function to see if it's an integer. If it is, the value is included in the output list. If not, it's skipped. The result is a new list containing only the integers from the original list.