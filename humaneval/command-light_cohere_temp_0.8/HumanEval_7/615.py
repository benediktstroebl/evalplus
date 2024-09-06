```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python script defines a function called **filter_by_substring** that filters an input list of strings to retain only those that contain a given substring.  The function uses the string and list comprehension to achieve this, and the time complexity is O(n) on average.