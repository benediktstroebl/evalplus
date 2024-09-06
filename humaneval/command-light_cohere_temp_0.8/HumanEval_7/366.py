Here is a self-contained Python script that implements the function `filter_by_substring` which solves the problem you described:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring

    Args:
        strings (List[str]): List of strings
        substring (str): Substring to filter

    Returns:
        List[str]: List of strings containing the given substring
    """
    return [string for string in strings if string.contains(substring)]
```

This script defines a function that filters a list of strings, returning a new list containing only the strings that contain the given substring. It utilizes the ideal use of the Python's typing module to provide type hints and make the code more readable.