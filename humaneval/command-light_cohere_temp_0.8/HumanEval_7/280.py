```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This Python code defines a function called `filter_by_substring`, which filters a list of strings and returns a new list containing only the elements that contain a given substring. The function uses the particular strings and substring as parameters and creates a new list with the filtered elements. This code is test can be used to solve the problem of filtering a list of strings for elements that contain a specific substring.