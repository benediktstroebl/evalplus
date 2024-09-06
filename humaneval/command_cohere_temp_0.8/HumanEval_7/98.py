```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code takes advantage of list comprehension to filter strings in the list that contain the given substring. It also adheres to the principle of the "Rule of Three" as it handles the input of two types: List[str] for the strings and substring: str for the substring.