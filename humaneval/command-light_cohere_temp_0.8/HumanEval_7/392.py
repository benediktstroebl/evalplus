```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This code defines a function that filters an input list of strings, returning a new list containing only the strings that contain the given substring.  The function uses the `find()` method from the string module to search for the substring within each string in the list.