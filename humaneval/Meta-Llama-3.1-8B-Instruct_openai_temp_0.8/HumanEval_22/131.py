```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    
    Args:
    values (List[Any]): A list of any python values.
    
    Returns:
    List[int]: A list of integers from the input list.
    
    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script defines a function `filter_integers` that takes a list of any Python values and returns a list of integers. It uses a list comprehension to filter out non-integer values. The `isinstance` function checks if a value is an instance of the `int` class. The script then tests the function with two examples.