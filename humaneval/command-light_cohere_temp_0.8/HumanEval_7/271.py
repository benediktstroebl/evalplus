Here's a self-contained Python script with a function that filters an input list of strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings for a substring

    Args:
        strings (List[str]): List of strings
        substring (str): Substring to filter

    Returns:
        List[str]: List of strings containing the substring
    """
    return [string for string in strings if string.contains(substring)]
```

This function utilizes the contains() method to check if each string in the input list contains the given substring. It then returns a