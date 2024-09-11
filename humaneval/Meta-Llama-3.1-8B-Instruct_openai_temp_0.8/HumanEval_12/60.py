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

    longest_str = strings[0]  # Initialize the longest string as the first string
    max_len = len(longest_str)  # Initialize the max length as the length of the first string

    for string in strings:
        if len(string) > max_len:  # If the length of the current string is greater than max_len
            longest_str = string  # Update the longest string
            max_len = len(string)  # Update the max length

    return longest_str  # Return the longest string

# Test cases
print(longest([]))  # Should return None

print(longest(['a', 'b', 'c']))  # Should return 'a'

print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'
```

Alternatively, you can solve this problem using the built-in `max` function with a custom key:

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

    return max(strings, key=len)  # Return the string with the maximum length

# Test cases
print(longest([]))  # Should return None

print(longest(['a', 'b', 'c']))  # Should return 'a'

print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'
```

This solution is more concise and efficient, as it leverages the optimized implementation of the `max` function.