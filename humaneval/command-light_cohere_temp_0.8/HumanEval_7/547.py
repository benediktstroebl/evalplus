```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This script defines a function `filter_by_substring` that filters an input list of strings, finding all occurrences of a given substring. It utilizes the specific characters, a List and a substring.