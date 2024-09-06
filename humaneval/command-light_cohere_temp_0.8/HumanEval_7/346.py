```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function, `filter_by_substring`, takes two parameters: a list of strings and a substring. It returns a using a list comprehension to filter out only the strings that contain the given substring.