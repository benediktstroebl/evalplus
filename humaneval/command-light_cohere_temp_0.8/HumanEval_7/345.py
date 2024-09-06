```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function, `filter_by_substring`, takes a list of strings and a substring as inputs. It uses the shallow list comprehension to iterate through the input strings and returns a new list containing only those strings that contain the given substring.