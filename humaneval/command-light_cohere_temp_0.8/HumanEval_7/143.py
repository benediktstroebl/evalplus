```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This script defines a function, `filter_by_substring`, that filters an input list of strings and returns a new list that contains only the strings that contain the given substring. The function uses the `find()` method from the string class to search for the substring in each string.