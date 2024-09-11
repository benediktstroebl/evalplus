```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): List of any python values

    Returns:
        List[int]: List of integers from the input list

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integers from the input list. The list comprehension inside the function uses the `isinstance` function to check if each value is an integer, and includes it in the new list if so. The example usage at the end demonstrates how to use this function with different inputs.