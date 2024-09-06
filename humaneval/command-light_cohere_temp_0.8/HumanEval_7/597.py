Here's a self-contained Python function that filters a list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The function uses the contains() method to check if each string in the list contains the given substring. This returns a words that contain the substring are returned from the list.