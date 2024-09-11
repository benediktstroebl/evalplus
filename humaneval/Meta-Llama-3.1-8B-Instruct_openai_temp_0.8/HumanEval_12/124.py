```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string or None if the input list is empty
    """

    # Check if the input list is empty
    if not strings:
        return None

    # Initialize the longest string as the first one in the list
    longest_str = strings[0]

    # Iterate over the list starting from the second string
    for s in strings[1:]:
        # If the current string is longer than the longest one found so far, update it
        if len(s) > len(longest_str):
            longest_str = s

    # Return the longest string
    return longest_str


# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. The function iterates over the list and keeps track of the longest string found so far. If a longer string is found, it updates the longest string. Finally, it returns the longest string. The test cases at the end of the script demonstrate the function's behavior.