```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list of any python values.

    Returns:
    List[int]: A list of integers from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))
# Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))
# Output: [1, 2, 3]
```

In this script, we're using a list comprehension to create a new list that only includes the values from the input list that are instances of the `int` type. The `isinstance()` function is used to check if a value is an instance of a particular class.