Here's a Python script with a self-contained function that filters an input list of strings for those containing a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This function uses the `find()` method to check if each string in the input list contains the given substring. It returns a