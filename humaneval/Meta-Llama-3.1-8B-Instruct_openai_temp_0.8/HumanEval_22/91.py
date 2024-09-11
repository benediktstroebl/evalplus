```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): A list of any python values
    
    Returns:
        List[int]: A list of integers from the input list
    
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

This Python script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integers from the original list. The function uses a list comprehension to filter the values. The `isinstance(value, int)` expression checks if a value is an integer, and only values for which this expression is `True` are included in the output list. The script also includes some test cases to demonstrate the function's behavior.