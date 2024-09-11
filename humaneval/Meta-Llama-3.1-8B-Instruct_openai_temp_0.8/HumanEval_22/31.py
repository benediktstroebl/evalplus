```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    
    Args:
    values (List[Any]): A list containing any type of Python values.
    
    Returns:
    List[int]: A list containing only the integers from the input list.
    
    Example:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage
print(filter_integers(['a', 3.14, 5]))
# Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))
# Output: [1, 2, 3]
```

In this script, we define a function `filter_integers` that takes a list of any type of Python values as input and returns a new list containing only the integers from the input list. We use a list comprehension to create this new list. The `isinstance` function checks whether a given value is an integer or not.