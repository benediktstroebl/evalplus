```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list containing any type of python objects

    Returns:
        List[int]: A list of integers filtered from the input list
    """
    return [value for value in values if isinstance(value, int)]

# Example usage
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This Python script uses a list comprehension to filter the input list for integers. The `isinstance(value, int)` function checks if each value in the list is an integer. If it is, the value is included in the output list.