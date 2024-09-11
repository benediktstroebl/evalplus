### Concatenating a List of Strings in Python
#### Problem Statement

Given a list of strings, write a function to concatenate them into a single string.

#### Solution

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

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
```

#### Explanation

The `concatenate` function takes a list of strings as input and uses the built-in `join` method of the string class to concatenate them. The `join` method takes an iterable of strings and concatenates them into a single string, with the string on which the method is called being used as a separator. Since we want to concatenate the strings without any separator, we pass an empty string to the `join` method.

You can test the function by running the script and calling the function with different inputs:

```python
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['hello','', 'world']))  # Output: 'hello world'
```