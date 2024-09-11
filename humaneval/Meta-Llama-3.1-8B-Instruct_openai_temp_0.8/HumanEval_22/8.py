```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
    values (List[Any]): A list of values of any Python type.

    Returns:
    List[int]: A list containing only the integer values from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integer values from the input list. The function uses list comprehension to create the new list. The `isinstance(x, int)` function is used to check if each value `x` is an integer. If it is, `x` is included in the new list. 

The script also includes two test cases to demonstrate the function's behavior.