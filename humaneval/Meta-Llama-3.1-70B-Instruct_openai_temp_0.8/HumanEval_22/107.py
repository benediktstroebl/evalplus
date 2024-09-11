```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any python values.

    Returns:
        List[int]: A list of integers filtered from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([]))  # Output: []
print(filter_integers([1.2, 3.4, '5']))  # Output: []
print(filter_integers([1, 2, '3', None]))  # Output: [1, 2]
```