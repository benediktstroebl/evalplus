```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any type of python values.

    Returns:
        List[int]: A list containing only the integers from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

This script defines a function `filter_integers` that uses list comprehension to iterate over the input list `values` and includes only those values that are instances of the `int` type. The `isinstance(value, int)` function checks if a value is an integer. The function returns the resulting list of integers.

The test cases at the end of the script demonstrate how the function works with different inputs, and the comments explain what output to expect.