```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python code defines a function `filter_by_substring` that filters a list of strings to include only those that contain a given substring.  It takes using a time, and efficiently checks each string in the list for the presence of the provided substring using the `find()` method. The function returns a list of remaining strings after removing the ones that don't contain the substring.