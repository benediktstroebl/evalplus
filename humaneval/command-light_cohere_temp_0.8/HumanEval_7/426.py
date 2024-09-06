```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the contains() method to check if each string in the input list contains the given substring, and then returns a new list containing only those strings.  It requires that the string and substring are both provided as arguments.