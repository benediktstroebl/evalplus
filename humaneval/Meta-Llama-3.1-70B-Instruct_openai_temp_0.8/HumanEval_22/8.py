```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any python values.

    Returns:
        List[int]: A list of integers filtered from the input list.
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

This script uses a list comprehension to create a new list that only includes the values from the input list that are instances of the `int` type. The `isinstance` function is used to check if a value is an integer.