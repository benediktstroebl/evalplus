Here's a self-contained Python function that filters an input list of strings for a given substring: 

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the contains method of the string class to check if each string contains the given substring. It returns a