```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses the starts-with operator to filter a list of strings, based on whether each string starts with the given prefix.