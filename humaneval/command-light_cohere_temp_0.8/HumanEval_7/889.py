```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The code you've shared appears to be a self-contained Python function that filters an input list of strings to retain only those that contain a given substring. It employs the string.s.find() method from method to efficiently locate the substring within each string in the list.