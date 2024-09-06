```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code takes advantage of list comprehension to filter strings that contain the given substring from the given list of strings.

This solution should allow the specification of the substring to search for as an argument, as well as the list of strings to search through. i.e. `filter_by_substring(['hello world', 'foo bar', 'goodbye'], 'good')` would return `['goodbye']`.