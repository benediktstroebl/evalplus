```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This script provides a self-contained solution for the problem, which is a function that filters an input list of strings for those that contain a given substring. 

Note that this is a simple implementation. It uses the `find()` method to check if a string contains the substring.