```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This code provides a function filter_by_prefix that filters an input list of strings based on a given prefix. The function utilizes the filtration technique, checking if each element's starting character matches the provided prefix. The resulting filtered list contains only the strings starting with the given prefix.