```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This script defines a function that filters an input list of strings, returning a new list that contains only the strings that contain the given substring. The code is self-contained, it uses the List[str] and str types, and the find method to check if each string in the input list contains the given substring.