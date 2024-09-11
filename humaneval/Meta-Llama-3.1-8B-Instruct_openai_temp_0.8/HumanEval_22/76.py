```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of mixed data types

    Returns:
        List[int]: A list of integers from the original list

    Example:
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

In this script, we use a list comprehension to create a new list that only includes the values from `values` that are instances of `int`. The `isinstance()` function checks if a value belongs to a particular class, and `int` is the class of all integers in Python. 

This solution is concise, readable, and adheres to the Do Not Repeat Yourself (DRY) principle by avoiding redundant code. The function is well-documented with a docstring that includes a description, parameters, return value, and example usage.