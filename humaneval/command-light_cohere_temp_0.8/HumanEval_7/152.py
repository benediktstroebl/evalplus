```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings for a given substring.

    Parameters:
    strings: list of strings
    substring: string to filter for

    Returns: filtered list of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```

This function uses a list comprehension to iterate over each string in the input list, and checks if the string contains the given substring. The function returns a list of strings that contain the substring. 

Would you like to know how to solve any other problems related to Python, coding, algorithms, or any other topics?