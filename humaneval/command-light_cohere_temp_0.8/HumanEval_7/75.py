```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This Python script defines a function `filter_by_substring` that filters a list of strings to only include those that contain a given substring. The function uses the `find()` method to check if a given substring exists in a string, and returns the list of matching strings.