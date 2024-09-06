Here is a Python script with a self-contained function that solves the problem of filtering strings that contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings that contain the given substring
    :param strings: list of strings
    :param substring: substring to filter
    :return: list of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```

This function takes two arguments: a list of strings and a substring to filter. The function uses the string method `contains` to check if each string in the list contains the given substring. The function then returns a list of strings that contain the substring. 

This function is self-contained and does not require any external functions or classes.