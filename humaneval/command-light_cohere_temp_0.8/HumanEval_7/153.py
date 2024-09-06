```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

The code defines a `filter_by_substring` function that filters an input list of strings and returns only the ones that contain the given substring using the `find` method.  The function is tested using a set of test strings that pass the filter.