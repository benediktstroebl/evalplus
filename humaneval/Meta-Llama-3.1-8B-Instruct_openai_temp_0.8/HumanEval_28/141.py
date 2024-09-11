### Concatenating List of Strings into a Single String
#### Problem Description
Write a Python function `concatenate` that takes a list of strings as input and returns a single string by concatenating all the input strings.

#### Solution
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: A single string by concatenating all the input strings

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Use the join method of the empty string to concatenate all strings in the list
    return ''.join(strings)
```

#### Explanation
This solution uses the `join` method of the empty string (`''.join()`) to concatenate all the strings in the input list. The `join` method takes an iterable of strings as input and returns a single string by concatenating all the input strings.

#### Example Usage
```python
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World', '!']))  # Output: 'Hello World!'
```