```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script provides a function called `filter_by_prefix` that filters an input list of strings and returns only those that start with a specified prefix. It uses the template syntax `List[str]` to iterate through the list of strings and uses the `startswith` method of the string object to check if each string starts with the given prefix.