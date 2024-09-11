```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: The concatenated string.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
print(concatenate(['Foo', 'Bar', 'Baz']))  # Output: 'FooBarBaz'
```

In this script, we define a function `concatenate` that takes a list of strings and returns their concatenation using the `join` method of an empty string. The `join` method concatenates all the strings in the list into one string. The script also includes some test cases to demonstrate the function's behavior.