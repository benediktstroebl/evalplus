```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list that can contain any type of python object

    Returns:
    List[int]: A list containing only the integer values from the input list

    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([1.2, 3.4, 5.6, 7.8]))  # []
print(filter_integers([True, False, None]))  # []
print(filter_integers([]))  # []
print(filter_integers([1, '2', 3.0, {}]))  # [1, 3]
```