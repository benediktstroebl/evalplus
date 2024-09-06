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
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result
```

The function `filter_integers` takes a list of values of any type as an argument and returns a list of integers. It iterates through each value in the input list, and if the value is an integer, it gets appended to the `result` list. Ultimately, this returns the `result` list containing only the integers from the given input.

This approach allows the function to handle different types of inputs, such as numeric and string values, as well as nested data types like dictionaries and lists, without causing any issues. It precisely captures the intent of the requested function: to filter integers from a list of diverse values.