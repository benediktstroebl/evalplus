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

    # Initialize the longest string with the first string in the list
    longest_str = strings[0]

    # Iterate over the rest of the strings in the list
    for s in strings[1:]:
        # If the current string is longer than the longest string found so far, update the longest string
        if len(s) > len(longest_str):
            longest_str = s

    # Return the longest string found
    return longest_str


# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print None
    print(longest(['a', 'b', 'c']))  # Should print 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```

This script defines a function `longest` that takes a list of strings and returns the longest one. If there are multiple strings of the same length, it returns the first one. If the input list is empty, it returns `None`. The script then includes some test cases to verify that the function behaves correctly.