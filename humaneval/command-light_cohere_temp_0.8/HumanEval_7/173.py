Here is a Python script that includes a self-contained function `filter_by_substring` which filters a list of strings based on whether the string contains a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of strings to filter
        substring (str): Substring to search for

    Returns:
        List[str]: List of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```

This script provides a simple and clear way to filter a list of strings based on whether they contain a given substring.