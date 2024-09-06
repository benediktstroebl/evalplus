Here is a self-contained Python function that filters an input list of strings for those containing a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The function takes a list of strings and a substring as input and returns a new list that contains only the strings from the input list that contain the given substring.