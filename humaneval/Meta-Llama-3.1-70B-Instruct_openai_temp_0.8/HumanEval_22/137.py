```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list containing any python values

    Returns:
        List[int]: A list containing only integers from the input list

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

This script defines the function `filter_integers` which uses a list comprehension to iterate over each value in the input list. It checks if each value is an instance of the `int` type using the `isinstance` function. If the value is an integer, it is included in the output list. The function returns the list of integers.

The script also includes test cases to verify the function's behavior.