```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
The `filter_by_substring` function filters an input list of strings and returns only the ones that contain the given substring.