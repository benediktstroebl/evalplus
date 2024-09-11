### Concatenate List of Strings into a Single String

Here is a Python script that solves the problem:
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single string that is the result of concatenating all the input strings

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)
```
This script uses the built-in `join()` function to concatenate all the strings in the input list into a single string. If the input list is empty, an empty string is returned, as specified in the problem statement. 

You can test the function with the provided examples:
```python
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```