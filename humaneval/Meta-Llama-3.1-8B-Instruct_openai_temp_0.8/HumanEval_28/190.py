### Concatenating List of Strings
#### Problem Statement

Concatenate a list of strings into a single string.

#### Solution

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

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
    # Use the join() method, which concatenates all strings in the list
    # The join() method requires a separator, in this case an empty string
    return ''.join(strings)
```

#### Explanation

This solution uses the `join()` method of the string class, which concatenates all the strings in the list. The `join()` method requires a string separator, in this case an empty string `''`, which effectively concatenates the strings without any separator. This solution has a time complexity of O(n), where n is the total number of characters in all strings, because the `join()` method creates a new string that is a copy of all the strings in the list.