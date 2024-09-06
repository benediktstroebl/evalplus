```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This Python script defines a function called `filter_by_substring`, which filters a list of strings to only include those that contain a given substring. The function utilizes the required list and substring typing to ensure type-safe operations and returns a new list containing only the strings that match the substring.