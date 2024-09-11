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
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
    print(filter_integers([]))  # []
    print(filter_integers([True, False, None]))  # []
```

This script uses a list comprehension to filter the input list. The `isinstance(value, int)` function checks if a value is an integer. If it is, the value is included in the output list. If not, it is skipped.