Here is a self-contained Python script that defines a function `filter_by_substring` that solves the problem of filtering strings that contain a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This script takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring.