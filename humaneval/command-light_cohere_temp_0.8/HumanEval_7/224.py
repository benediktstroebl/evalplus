Here is a Python script that contains a self-contained function that filters an input list of strings for a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script provides a useful function that filters an input list of strings to only those that contain the given substring.