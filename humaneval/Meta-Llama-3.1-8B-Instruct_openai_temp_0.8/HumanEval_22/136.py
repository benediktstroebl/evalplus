### Filtering Integers from a List of Mixed Values
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing mixed values.

    Returns:
        List[int]: A list containing only the integers from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]
```
This script uses a list comprehension to create a new list containing only the integers from the input list. The `isinstance()` function checks whether each value in the list is an instance of the `int` class.