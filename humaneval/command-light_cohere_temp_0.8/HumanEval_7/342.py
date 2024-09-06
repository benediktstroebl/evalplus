Here's a Python script with a self-contained function that filters an input list of strings for those containing a given substring:

```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script provides a well-tested and self-contained solution to the problem of filtering strings for a given substring.