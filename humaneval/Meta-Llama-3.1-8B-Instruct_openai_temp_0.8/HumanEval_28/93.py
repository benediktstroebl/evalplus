```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: The concatenated string

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join method to concatenate the strings in the list
    # The join method takes an iterable of strings and concatenates them with the string it's called on in between each pair of strings
    # In this case, we call join on an empty string, so no characters are inserted between the strings
    return ''.join(strings)
```

This script defines a function `concatenate` that takes a list of strings and returns their concatenation. The `join` method is used to concatenate the strings, which is more efficient than using the `+` operator to concatenate strings in a loop. 

You can test this function with the examples provided in the docstring by running the script and using the `>>>` prompt in a Python interpreter.