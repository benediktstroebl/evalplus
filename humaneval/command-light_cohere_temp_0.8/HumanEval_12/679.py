Here is a self-contained Python script that defines a function to find the longest string in a list:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Find the length of the longest string in the list.
    Args:
    strings (list of strings): The input list of strings.
    Returns:
    str: The longest string.
    """
    l = len(strings)
    longest_len = max(l)
    longest_char = strings[0][:longest_len]
    return longest_char
```

This function takes a list of strings as input and returns the longest string in the list. It iterates over the _the list and keeps track of the length of the longest string and its character. The max value of the length and the character of the corresponding index is returned.