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
    for string in strings[1:]:
        # Check if the current string is longer than the longest string found so far
        if len(string) > len(longest_str):
            # If it is, update the longest string
            longest_str = string
    
    # Return the longest string
    return longest_str

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

Alternatively, you can use the built-in `max` function with a custom key to make the code more concise:

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
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```