```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from a list of strings.
    Parameters:
    strings (List[str]): List of strings

    Returns:
    List of strings, longest one.
    """
    # Sort strings in descending order
    sorted(strings, reverse=True)
    # Find the length of the longest string
    max_length = max(len(string) for string in strings)
    # Initialize the longest string and return it
    longest = strings[0]
    for string in strings:
        # Check if the length of the current string is greater than the current length of the longest string
        if len(string) > max_length:
            # Update the longest string
            longest = string
            # Update the max length
            max_length = len(string)
    return longest
```