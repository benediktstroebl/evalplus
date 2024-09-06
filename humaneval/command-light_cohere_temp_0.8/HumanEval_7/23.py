```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python code defines a function `filter_by_substring` that filters a list of strings to retain only those that contain a given substring. It uses the strategic use of the `contains` to iterate over the strings and check if each one contains the given `substring`.