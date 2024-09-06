```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This function employs the contains() method to traverse the input strings and filter those that contain the given substring.  The return a list containing the strings that passed the filter.