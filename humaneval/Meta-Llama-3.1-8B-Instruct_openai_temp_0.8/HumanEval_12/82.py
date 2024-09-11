```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty.
    """
    # Check if the list is empty
    if not strings:
        return None
    
    # Use the max function with a custom key to find the longest string
    return max(strings, key=len)


# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This Python script defines a function called `longest` that takes a list of strings and returns the longest one. If the list is empty, it returns `None`. The function uses the built-in `max` function with a custom key to find the longest string. The key function, `len`, is used to determine the length of each string. If there are multiple strings of the same length, the `max` function returns the first one it encounters.