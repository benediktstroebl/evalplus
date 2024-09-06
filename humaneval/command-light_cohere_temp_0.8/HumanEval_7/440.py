```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python script defines a function `filter_by_substring` that filters a list of strings to only include those that contain a given substring.  The input is a list of strings and a substring, and the output is a new list containing only the strings that contain the substring. 

The function utilizes the Python's `contains` method to check if each string in the input list contains the given substring.