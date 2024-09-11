```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list of python values.

    Returns:
        List[int]: A list of integers.
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integers. The `isinstance(value, int)` function checks if each value is an integer, and if it is, it is included in the new list.

The test cases demonstrate the function's behavior with different inputs.