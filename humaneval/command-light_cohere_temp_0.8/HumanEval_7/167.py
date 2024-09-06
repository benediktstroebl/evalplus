```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This code implements a function **filter_by_substring** that filters an input list of strings and returns only the elements that contain a given substring. 

It uses the `find()` function which looks for a substring within a string.