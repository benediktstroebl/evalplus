```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty
    """
    if not strings:  # Check if the list is empty
        return None
    else:
        return max(strings, key=len)  # Return the longest string


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

In this code, we use the built-in `max` function in Python, which has a `key` argument that allows us to specify a function to be called on each list element prior to making comparisons. We use `len` as the `key` function to find the longest string. If the list is empty, `max` returns `inf` which is not what we want, so we handle this case explicitly.