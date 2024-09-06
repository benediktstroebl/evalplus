```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This function uses the `find()` method to search for the given substring in each string. It returns a recent list of strings that contain the given substring.