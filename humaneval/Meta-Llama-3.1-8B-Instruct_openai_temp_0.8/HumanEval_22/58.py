```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): List of any python values
    
    Returns:
        List[int]: List of integers from the input list
    
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

In this script, we define a function `filter_integers` that takes a list of any Python values as input and returns a new list containing only the integers from the input list. The function uses a list comprehension to achieve this.

The `isinstance` function is used to check if each value in the input list is an instance of the `int` type. If it is, the value is included in the new list; otherwise, it is skipped.