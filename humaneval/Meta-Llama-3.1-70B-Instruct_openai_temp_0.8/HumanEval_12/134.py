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

    # Check if the input list is empty
    if not strings:
        return None  # Return None if the list is empty

    # Initialize the longest string as the first string in the list
    longest_str = strings[0]

    # Iterate over the list of strings
    for string in strings:
        # Check if the current string is longer than the longest string
        if len(string) > len(longest_str):
            longest_str = string  # Update the longest string

    return longest_str  # Return the longest string

# Test the function
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```

Alternatively, you could use the built-in `max` function with a key argument to make the function more concise:

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

    # Check if the input list is empty
    if not strings:
        return None  # Return None if the list is empty

    # Use the max function with a key argument to find the longest string
    return max(strings, key=len)

# Test the function
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```