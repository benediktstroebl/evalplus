```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function called `filter_by_prefix` that filters an input list of strings to only include those that start with a specified prefix. The function uses the filter technique where it uses the `startswith` method of the string to check if each string starts with the given prefix. The function then returns a list of the filtered strings.