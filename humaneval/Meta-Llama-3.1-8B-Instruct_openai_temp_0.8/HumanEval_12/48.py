```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    else:
        return max(strings, key=len)  # Return the longest string in the list


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This Python script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the list is empty, it returns `None`. The `max` function with the `key=len` argument is used to find the longest string. The test cases are included to demonstrate the functionality of the `longest` function.