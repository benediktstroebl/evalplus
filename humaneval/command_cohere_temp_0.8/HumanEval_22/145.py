```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter a list of values down to only integers.

    Args:
        values (List[Any]): The list of values to filter.

    Returns:
        List[int]: A new list containing only the integers from the input list.

    Example:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]
```

The function `filter_integers` takes a list of values and returns a new list that includes only the integer values present in the input list. The function utilizes Python's list comprehension feature along with the `isinstance()` function to identify and filter out non-integer elements. 

This solution aligns with Python's typing module to ensure type safety and facilitate code comprehension. Test cases are also included to verify the function's behavior against different input scenarios.