Here's a self-contained Python script that implements the filter_by_substring function as described:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This script defines a function that takes a list of strings and a substring as arguments. It then uses the's a list comprehension to filter the strings list and return only the ones that contain the given substring.