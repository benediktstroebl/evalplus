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
    # If the list is empty, return None
    if not strings:
        return None
    
    # Use the max function with the key argument set to len to find the longest string
    # The max function returns the first string in case of a tie
    return max(strings, key=len)

# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the input list is empty, it returns `None`. The function uses the built-in `max` function with the `key` argument set to `len` to find the longest string. If there are multiple strings of the same maximum length, the `max` function returns the first one, as required by the problem statement.