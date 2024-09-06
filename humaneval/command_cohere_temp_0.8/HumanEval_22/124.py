```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter a given list of any Python values only for integers.

    Args:
        values (List[Any]): The input list of values of any type.

    Returns:
        List[int]: A list containing only the integer values present in the input list.

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

The function `filter_integers` takes a list of values of any type as an argument and returns a list of integers present in the input list. It does so by iterating through each value in the input list using a for loop. It checks if each value is an instance of the integer class using the `isinstance` function, and if so, it appends the value to the `integer_values` list. Finally, the function returns the `integer_values` list. 

Note that the function is designed to work with Python versions earlier than Python 3.9 and those compatible with PEP 560. For newer Python versions, use the `type:` annotation described in the Type Hinting section of the official Python documentation.