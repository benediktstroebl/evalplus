```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any python values.

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
print(filter_integers(['a', 3.14, 5]))  # Expected: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected: [1, 2, 3]
```

This script defines a function `filter_integers` that uses list comprehension to create a new list containing only the integers from the input list. The `isinstance` function is used to check if each value is an integer. The script also includes test cases to validate its correctness.