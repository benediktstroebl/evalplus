```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain the given substring"""
    return [string for string in strings if string. contains.find(substring)]


```

This Python function, `filter_by_substring`, takes a list of strings and a substring as input and returns a new list of strings that contain the substring. It uses the unique method of filtering, which involves checking each string in the list for the presence of the substring using the `find()` method of the string.