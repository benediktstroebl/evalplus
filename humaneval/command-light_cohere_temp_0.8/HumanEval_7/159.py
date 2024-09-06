Here's a self-contained Python function that filters an input list of strings for ones that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The function uses the contains() method of the string object to check if each string contains the given substring.