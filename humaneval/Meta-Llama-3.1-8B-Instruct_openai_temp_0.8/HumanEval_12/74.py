```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the input list is empty.
    """
    if not strings:  # Check if the list is empty
        return None

    longest_str = strings[0]  # Initialize the longest string as the first string in the list
    max_len = len(longest_str)  # Initialize the maximum length as the length of the first string

    for string in strings:  # Iterate over the list of strings
        if len(string) > max_len:  # Check if the current string is longer than the longest string
            longest_str = string  # Update the longest string
            max_len = len(string)  # Update the maximum length

    return longest_str  # Return the longest string

# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print None
    print(longest(['a', 'b', 'c']))  # Should print 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```

This script first checks if the input list is empty. If it is, the function returns None. If the list is not empty, it initializes the longest string as the first string in the list and the maximum length as the length of the first string. It then iterates over the list of strings, checking if each string is longer than the current longest string. If a longer string is found, it updates the longest string and the maximum length. Finally, it returns the longest string.