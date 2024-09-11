```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list containing any python values

    Returns:
    List[int]: A list containing only integers from the input list
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected: [1, 2, 3]
```

This script uses a list comprehension to iterate over the input list and includes only the values that are instances of `int` type, effectively filtering out non-integer values. The `isinstance(value, int)` function checks if a value is an instance or subclass of the `int` class.