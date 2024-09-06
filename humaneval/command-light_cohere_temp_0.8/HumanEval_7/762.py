```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This Python code defines a function named **filter_by_substring** that filters and returns a new list of strings from the input list **strings** that contain a given substring.  The substring is compared to each string using the **find()** method. 

This function is self-contained and solves the problem of filtering strings based on a substring.