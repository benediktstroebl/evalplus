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
    if not strings:
        return None  # Return None if the list is empty

    longest_str = strings[0]  # Assume the first string is the longest
    max_len = len(longest_str)  # Keep track of the maximum length

    for s in strings:
        if len(s) > max_len:  # If a string is longer than the current longest
            longest_str = s  # Update the longest string
            max_len = len(s)  # Update the maximum length

    return longest_str  # Return the longest string


# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None

    print(longest(['a', 'b', 'c']))  # Should print: 'a'

    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This Python script defines the `longest` function that takes a list of strings and returns the longest string. If the input list is empty, it returns `None`. If there are multiple strings of the same maximum length, it returns the first one it encounters. The script includes test cases to demonstrate its correctness.