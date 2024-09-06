```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python code defines a function `filter_by_substring` that filters a list of strings to only include those that contain a given substring. It uses the `contains` method, where the `in` parameter is a list of strings and the `substring` parameter is the substring to find. The code uses the filter function to create a new list of strings that contain the given substring.