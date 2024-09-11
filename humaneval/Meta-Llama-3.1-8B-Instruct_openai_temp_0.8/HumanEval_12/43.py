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

    # Check if the list is empty, return None in this case
    if not strings:
        return None

    # Initialize the longest string with the first string in the list
    longest_str = strings[0]

    # Iterate over the list of strings
    for s in strings:
        # If the current string is longer than the longest string found so far, update the longest string
        if len(s) > len(longest_str):
            longest_str = s

    # Return the longest string
    return longest_str

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

Alternatively, you could use the built-in `max` function with a key function that returns the length of each string. This approach is more concise and Pythonic:

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.
    """

    # If the list is empty, return None
    if not strings:
        return None

    # Use max with a key function to find the longest string
    return max(strings, key=len)

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```