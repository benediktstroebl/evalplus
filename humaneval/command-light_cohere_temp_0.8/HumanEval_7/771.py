Here's the self-contained Python script with the function `filter_by_substring` that meets your requirements:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings and return those that contain a given substring.
    Parameters:
    strings: list of strings
    substring: the substring to search for
    Returns: list of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```

The function utilizes the contains method from the string module to check if each string in the input list contains the given substring. The results are a list of strings that contain the substring.