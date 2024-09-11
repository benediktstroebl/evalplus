```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any python values

    Returns:
        List[int]: A list of integers

    Example:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([]))  # Output: []
print(filter_integers([1, 2, 'a', 3, 'b', 4, 5.5]))  # Output: [1, 2, 3, 4]
```

This function uses list comprehension to create a new list that includes only the integers from the original list. The `isinstance(value, int)` function checks if each value in the list is an integer. The function returns this new list.