```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from the list.
    Args:
        strings (List[str]): List of strings.
    Returns: list of all strings, or None in case of empty list.
    Returns the longest string.
    """
    long_strings = []
    for string in strings:
        if len(string) > len(long_strings):
            long_strings.append(string)
        return long_strings[0]
    """
    return longest([]) 

longest(['a', 'b', 'c']) 
```
Do you have any other questions related to Python programming or specific algorithms?