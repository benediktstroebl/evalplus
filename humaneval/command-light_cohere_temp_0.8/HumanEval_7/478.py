```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The code defines a function called `filter_by_substring` that takes a list of strings and a substring as input. It uses the` contains()` to filter the list and return only the strings that contain the specified substring.