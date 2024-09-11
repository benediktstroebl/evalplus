### Concatenating List of Strings
#### Problem Statement
Given a list of strings, write a function `concatenate` that returns a single string by concatenating all the strings in the list.

#### Solution
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings

    Returns:
        str: A single string by concatenating all strings in the list

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join function to concatenate all strings in the list
    # The join function takes an iterable of strings and concatenates them
    # The separator argument is an empty string, which means no separator is used
    return ''.join(strings)
```

#### Explanation
The `concatenate` function uses the built-in `join` function from Python's `str` class to concatenate all strings in the input list. The `join` function takes an iterable of strings and concatenates them with the specified separator. In this case, we use an empty string as the separator to concatenate the strings without any separator. If the input list is empty, the `join` function returns an empty string.

#### Example Use Cases
```python
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
print(concatenate(['Python', 'is', 'awesome!']))  # Output: 'Pythonisawesome!'
print(concatenate([]))  # Output: ''
```