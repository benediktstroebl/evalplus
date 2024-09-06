```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This Python function takes a list of strings and a substring as input, then returns a new list containing only the strings that contain the given substring. It uses the basic list comprehension to filter the strings that contain the substring.