```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input. It uses the search the language-specific technique to return a new list containing only the strings from the input list that contain the given substring.