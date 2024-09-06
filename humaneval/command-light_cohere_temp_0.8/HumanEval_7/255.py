Here's a self-contained Python script with a function `filter_by_substring` that filters an input list of strings for ones that contain a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the `contains` method of a string to check if each element of the input list contains the given substring.  It uses a string's `List` and `str` types.