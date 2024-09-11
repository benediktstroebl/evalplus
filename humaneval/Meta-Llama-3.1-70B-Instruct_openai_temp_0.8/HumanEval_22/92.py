```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any python values

    Returns:
        List[int]: A list of integers filtered from the input list
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

This script uses a list comprehension to iterate over the input list `values`. The `isinstance(value, int)` condition checks if each value is an integer. If it is, the value is included in the output list. The result is a new list that contains only the integers from the original list.