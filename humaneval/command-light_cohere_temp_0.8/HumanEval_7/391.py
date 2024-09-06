```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This code implements a function that filters a list of strings, returning a new list containing only the strings that contain the given substring.