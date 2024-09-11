```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any type of python values.

    Returns:
        List[int]: A list of integers from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Test the function with provided examples
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

This Python script defines a function called `filter_integers` that filters a list of any type of Python values (List[Any]) and returns a new list containing only the integers (List[int]) from the input list. The function uses a list comprehension to achieve this. It also includes docstrings and test cases to demonstrate its usage and behavior.