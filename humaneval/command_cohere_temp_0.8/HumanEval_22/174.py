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

The function `filter_integers` takes a list of values of any type as an argument and returns a list of integers. It iterates through each value in the input list and adds it to the result list only if it is an instance of the integer type. Finally, it returns the result list.

This solution includes type hints, which not only improve code readability but also provide hints to the Python interpreter for runtime type checking. The added type hint `Optional[List[int]]` to the return type of the function indicates that the function returns a list of integers, or optionally, an empty list. This allows for some flexibility when calling the function to handle cases where no integers are found in the input list.