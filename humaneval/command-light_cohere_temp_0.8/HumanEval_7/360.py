```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This script defines a function that filters an input list of strings for a given substring. It uses the `find()` method with the substring as the search value to check if each string contains the substring.