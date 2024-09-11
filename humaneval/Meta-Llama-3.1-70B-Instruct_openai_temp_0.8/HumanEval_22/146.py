```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values: A list of any python values.

    Returns:
        A list of integers.
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```
This script uses list comprehension to create a new list containing only the values that are instances of integers. The `isinstance(value, int)` function checks if a value is an integer. If it is, the value is included in the new list; otherwise, it is skipped.