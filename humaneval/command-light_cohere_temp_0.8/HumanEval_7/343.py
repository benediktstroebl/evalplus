```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This function iterates through a list of strings and returns a new list containing only the strings that contain the given substring. It utilizes the search.js' find() method to locate all occurrences of the substring in each string.