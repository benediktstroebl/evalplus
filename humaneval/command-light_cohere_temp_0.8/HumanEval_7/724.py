Here's the solution to the markdown code block problem using Python:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring

    Args:
        strings (List[str]): List of strings to filter
        substring (str): Substring to search for

    Returns:
        List[str]: List of strings containing the given substring
    """
    return [string for string in strings if string.contains(substring)]
```

This Python script defines a function `filter_by_substring` that filters a list of strings, returning a new list containing only the strings that contain the given substring. The function uses the critical type hint `typing` to define the function parameters and return types, which allows for better code readability and future type-checking compatibility.