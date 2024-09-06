```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter a list of Python values to a list of integers.

    Args:
        values (List[Any]): A list of any Python values.

    Returns:
        List[int]: A list containing only integers from the input list.

    Example:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [val for val in values if isinstance(val, int)]
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It uses a list comprehension, iterating over each value `val` in the input `values`. It checks if `val` can be converted to an integer using the `isinstance` function, which returns `True` if the conversion is possible. This way, it filters out non-integer values and returns a list of integers.