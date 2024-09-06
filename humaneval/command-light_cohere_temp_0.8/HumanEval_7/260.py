Here is a Python script that includes the function `filter_by_substring`, which filters a list of strings based on a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function uses the the Python's `contains` method to check if a string contains the given substring, and then returns the string from the list.

This is a self-contained function that demonstrates the use of Python's `typing` and string manipulation.