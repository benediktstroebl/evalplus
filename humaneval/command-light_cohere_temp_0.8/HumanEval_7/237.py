```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This Python script defines a function called **filter_by_substring** that filters an input list of strings and returns a new list containing only the strings that contain the given substring. The function utilizes theas built-in **find** function to search for the substring in each string and returns the desired result.