```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python code defines a function called `filter_by_substring` that filters a list of strings based on whether the given substring is present in each string. It utilizes the filtering through List comprehension to achieve this and returns a new list containing only the strings that contain the given substring.