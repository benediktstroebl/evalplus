```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input. It uses the uses the Strings that contain the given substring are returned in a new list.