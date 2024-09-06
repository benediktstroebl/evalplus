Here is a self-contained Python script that solves the problem of filtering strings that contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This script provides a function that filters and returns a list of strings from an input list of strings, where each string contains the given substring. 

This is a self-contained solution and passes the corresponding tests without using any external libraries.