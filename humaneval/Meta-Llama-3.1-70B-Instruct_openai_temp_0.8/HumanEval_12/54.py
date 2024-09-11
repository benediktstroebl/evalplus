```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """

    # Check if the input list is empty
    if not strings:
        return None

    # Initialize the longest string with the first string in the list
    longest_str = strings[0]

    # Iterate over the rest of the strings in the list
    for string in strings[1:]:
        # Check if the current string is longer than the longest string found so far
        if len(string) > len(longest_str):
            # If it is, update the longest string
            longest_str = string

    # Return the longest string
    return longest_str


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

Alternatively, you can use the built-in `max` function with a key function to make the code more concise:

```python
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len, default=None)
```

This version of the function works the same way as the previous one, but it uses the `max` function to find the longest string in the list. The `key` argument is used to specify that the strings should be compared based on their lengths, and the `default` argument is used to specify that `None` should be returned if the list is empty.