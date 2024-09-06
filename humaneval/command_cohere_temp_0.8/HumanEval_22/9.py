```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter a given list of any Python values only for integers.

    Args:
        values (List[Any]): The input list of values of any type.

    Returns:
        List[int]: A list containing only the integers from the input list.

    Example:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    integer_values = []
    for value in values:
        if isinstance(value, int):
            integer_values.append(value)
    return integer_values
```

The function `filter_integers` takes a list of values of any type as an argument and returns a list of integers. It iterates through each value in the input list and checks if it is an instance of the integer class using the `isinstance` function. If it is, the value is appended to the `integer_values` list, which is returned at the end.

This implementation has a straightforward logic, closely related to the problem description, and should be easily understandable for other programmers. It also does not make any assumptions or restrictions on the input data other than it being a list, and the values in the list can be of any type. Thus, it covers all edge cases reasonably well.