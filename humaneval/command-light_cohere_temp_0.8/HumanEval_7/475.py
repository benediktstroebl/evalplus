```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring """
    return [string for string in strings if string.contains(substring)]
```

This function uses the contains() method to filter the strings in the list that contain the given substring.