### Concatenate List of Strings into a Single String

Here's a Python function that uses the `join()` method from the `str` class to concatenate a list of strings into a single string.

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: A single string that is the concatenation of all strings in the list

    Example use cases:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

In this script:

1. We import the `List` type from the `typing` module to specify the type of the `strings` parameter.
2. We define a function `concatenate` that takes a list of strings as input and returns a single string.
3. We use the `join()` method to concatenate the strings in the list. Since we want to concatenate strings without any separator, we pass an empty string to the `join()` method.
4. We include docstrings to explain the purpose of the function, its parameters, and its return value.
5. We test the function with two example use cases: concatenate an empty list and concatenate a list of three strings.