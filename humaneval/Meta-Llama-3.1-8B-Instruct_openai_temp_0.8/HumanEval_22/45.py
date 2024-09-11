```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

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
print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

This script defines the `filter_integers` function, which takes a list of any python values as input and returns a new list containing only the integers from the input list. The function uses a list comprehension to iterate over the input list and checks each value with the `isinstance` function to see if it's an integer. If it is, the value is included in the output list. 

The script also includes two example use cases at the end to demonstrate how to use the `filter_integers` function. 

Note that we define the function with type hints for better clarity and readability of the code. We also include a docstring with a description, arguments, return values, and examples of usage. This follows best practices for writing readable and maintainable code. 

The `isinstance` function is used to check the type of a value, and it returns `True` if the value is of the given type (or any subclass of the given type) and `False` otherwise. This is a concise and efficient way to check if a value is an integer in Python.