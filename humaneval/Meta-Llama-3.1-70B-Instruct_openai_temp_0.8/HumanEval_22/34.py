```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list of any python values.

    Returns:
        List[int]: A list of integers.
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script uses a list comprehension to filter the input list `values`. The `isinstance(value, int)` function checks if a value is an integer, and only includes it in the output list if it is. This approach is both efficient and easy to read.