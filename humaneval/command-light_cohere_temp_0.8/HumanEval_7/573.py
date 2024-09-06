```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings for the presence of a given substring.
    :param strings: list of strings
    :param substring: string to filter for
    :return: list of strings that contain the given substring
    """
    return [x for x in strings if x.contains(substring)]
```
This Python script defines a function called filter_by_substring that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The function uses a 'in' operator to check if each string in the input list contains the given substring, and the result is the list of strings that pass the filter.