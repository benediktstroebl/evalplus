Here's the provided self-contained Python function:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The function uses the contains() method from string objects to check if each string in the input list contains the given substring.