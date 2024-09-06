```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain the given substring.
    The Filtering is performed using a case-insensitive comparison.
    Returns a precise list of strings with substring
    """
    return [string for string in strings if string.contains(substring, True]
```
This Python code defines a function named filter_by_substring within a List[str] called strings, which contains a list of strings, and a str called substring. It uses the precise list comprehension with the contains() method to filter and return only the strings from the strings list that contain the substring substring, using a case-insensitive comparison. The code then also uses the filtered list to check if it is empty, and if it is not empty, it returns the list of strings with the substring.