```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
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
    return [x for x in values if isinstance(x, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of any Python values as input and returns a new list containing only the integers from the original list. The function uses a list comprehension to iterate over the input list and include only the values that are instances of the `int` type. The script includes docstrings to provide documentation for the function and includes test cases to verify its correctness.