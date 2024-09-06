Here's the solution:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
```

The function takes two parameters: `strings`, which is a list of strings, and `substring`, which is a substring to search for within the strings. The function returns a filter the list of strings that contain the given substring using a list comprehension.