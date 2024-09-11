```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): List of any python values

    Returns:
        List[int]: List of integers
    """
    return [value for value in values if isinstance(value, int)]


# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script uses a list comprehension to iterate over the input list `values`. It uses the `isinstance()` function to check if each value is an integer. If it is, the value is included in the output list. If not, it's skipped.