```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring.

    : Parameters:
        strings (List[str]) - list of strings to filter
        substring (str) - substring to search for

    Returns:
        filtered_strings (List[str]) - list of strings containing the substring
    """
    return [string for string in strings if string.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input. It uses the necessary in place to filter the strings in the list, returning a new list that only contains the strings that contain the given substring.