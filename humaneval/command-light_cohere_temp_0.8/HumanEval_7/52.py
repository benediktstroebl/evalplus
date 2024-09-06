Here is a self-contained Python script that solves the problem of filtering strings for a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings for the given substring
    :param strings: List of strings
    :param substring: Substring to filter
    :return: List of strings containing the given substring
    """
    return [string for string in strings if string.contains(substring)]
```

This script defines a `filter_by_substring` function that takes a list of strings and a substring as input, and returns a new list of strings that contain the given substring. 

The function uses the `contains` method, which checks if each string in the list contains the given substring.