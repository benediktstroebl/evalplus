```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

The solution uses the `find()` method to search each string in the input list for the given substring. The function returns a list of all the strings from the list that contain the substring.