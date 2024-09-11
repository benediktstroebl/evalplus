```markdown
### Longest String in a List

This script defines a function `longest` that takes a list of strings as input and returns the longest string. 
In case of multiple strings of the same length, it returns the first one. If the input list is empty, it returns `None`.

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None.
    """
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Return the longest string

# Test cases
import doctest
doctest.testmod()
```

### Explanation

- The function `longest` takes a list of strings as input and returns the longest one.
- We check if the list is empty using the condition `if not strings`. If it is, we return `None`.
- Otherwise, we use the built-in function `max` with the `key=len` argument to find the longest string. The `key` argument specifies a function of one argument that is used to extract a comparison key from each input element. In this case, we use `len` to extract the length of each string, and `max` returns the string with the maximum length. In case of multiple strings of the same length, `max` returns the first one.

### Usage

You can run the script and use the `longest` function to find the longest string in a list of strings. For example:

```python
print(longest(['a', 'b', 'c']))  # Output: 'c'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))  # Output: None
```