```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This function iterates through the input list of strings and returns a new list that contains only the strings that contain the given substring.  It uses the search method to find the substring in each string.