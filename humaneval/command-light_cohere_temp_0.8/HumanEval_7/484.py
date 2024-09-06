```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The function uses a list comprehension to filter the strings in the strings list, based on whether the string contains the given substring. The function returns a string list that contains only the strings from the original list that contain the given substring.