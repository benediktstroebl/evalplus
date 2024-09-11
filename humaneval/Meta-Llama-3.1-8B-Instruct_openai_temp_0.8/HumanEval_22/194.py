```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
    values (List[Any]): A list containing any type of python objects
    
    Returns:
    List[int]: A list containing only the integers from the input list
    
    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test the function
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This script defines a function `filter_integers` that uses list comprehension to filter a list of any Python objects and return a new list containing only the integers. The function uses the built-in `isinstance` function to check if each value in the list is an integer. If it is, the value is included in the new list; otherwise, it is skipped. The script then tests the function with two examples from the docstring.