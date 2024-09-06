Here's the self-contained Python script that solves the problem of filtering strings that contain a given substring: 

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain the given substring.
    Args:
    strings: list of strings
    substring: substring to search for in each string
    Returns: list of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```

This script provides a function that filters an input list of strings, returning only the strings that contain a given substring. 

Let me know if you'd like to explore other variations of coding problems or would like assistance with implementing another task!