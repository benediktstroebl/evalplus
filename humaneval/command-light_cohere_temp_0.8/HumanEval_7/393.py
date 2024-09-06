```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]
```

This script defines a function `filter_by_substring` that filters a list of strings, returning only the ones that contain the given substring. The test cases are provided to ensure that the function behaves as expected.