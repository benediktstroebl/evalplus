```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list of values that can be of any type.

    Returns:
        List[int]: A new list containing only the integers from the input list.

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
print(filter_integers([]))  # Output: []
```

In this code:

- The `filter_integers` function takes a list of any type of values as input.
- It uses a list comprehension to create a new list containing only the integers from the input list.
- The `isinstance(value, int)` function checks if a value is an integer.
- The function includes a docstring that describes its purpose, parameters, return values, and includes test cases as examples.