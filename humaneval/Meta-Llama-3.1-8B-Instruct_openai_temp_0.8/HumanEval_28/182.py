### Concatenating a List of Strings
#### Problem Description
Given a list of strings, write a function to concatenate them into a single string.

#### Solution
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: The concatenated string.

    Example:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join method to concatenate all strings in the list
    return ''.join(strings)
```
#### Explanation
The `join` method is a built-in string method in Python that concatenates all strings in an iterable (in this case, a list of strings) and returns a single string. The `''` argument to the `join` method indicates that no separator should be used between the concatenated strings. This approach is more efficient and elegant than using a loop to concatenate the strings.