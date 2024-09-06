Here's a self-contained Python function that filters an input list of strings for those containing a given substring: 
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This function uses the contains() method on strings to check if each string contains the given substring.