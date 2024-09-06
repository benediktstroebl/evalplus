```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python function, `filter_by_substring`, filters an input list of strings to only include those that contain a given substring. It uses the `find()` method to search for the substring within each string, and returns a new list containing only the matching strings.