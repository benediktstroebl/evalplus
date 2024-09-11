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
        Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:
        # If the list is empty, return None
        return None
    else:
        # Sort the list in descending order based on the length of the strings
        return max(strings, key=len)

# Test cases
print(longest([]))  # Should print: None

print(longest(['a', 'b', 'c']))  # Should print: 'a'

print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

In this script, the `longest` function first checks if the input list `strings` is empty. If it is, the function returns `None`. Otherwise, it uses the built-in `max` function with a custom key function `len` to find the longest string in the list. The `key` argument of `max` is used to specify that we want to compare the strings based on their lengths.