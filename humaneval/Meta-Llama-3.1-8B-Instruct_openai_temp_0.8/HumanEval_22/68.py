```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    
    Args:
    values: A list of any python values.
    
    Returns:
    A list of integers from the given list.
    
    Example:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers(['s', 'a', 'b', 'c']))  # Output: []
print(filter_integers([1, 2.5, 3]))  # Output: [1, 3]
```

In this script, we define a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integers from the original list. The function uses a list comprehension with the `isinstance` function to check whether each value in the list is an instance of the `int` class. If it is, the value is included in the new list; otherwise, it is skipped.