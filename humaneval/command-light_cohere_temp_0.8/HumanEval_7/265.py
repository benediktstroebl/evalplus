Below is a self-contained Python script with a function that filters an input list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings and return those that contain the given substring
    :param strings: list of strings
    :param substring: substring to filter for
    :return: list of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```

This script defines a function `filter_by_substring` that takes two parameters: a list of strings and a substring. The function uses the `contains` in Python.

The function then iterates through the list of strings and returns a new list that contains only the strings that contain the given substring.