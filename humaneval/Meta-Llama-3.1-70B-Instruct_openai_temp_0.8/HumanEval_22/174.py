```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list containing various python values.

    Returns:
    List[int]: A list containing only integers from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```
This script defines a function `filter_integers` that filters a given list of values and returns a new list containing only the integers from the original list. The function uses a list comprehension and the `isinstance` function to check if each value is an integer. The script also includes example use cases to demonstrate the function's behavior.