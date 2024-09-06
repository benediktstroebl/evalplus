```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


# Tests
strings = ['abc', 'bcd', 'cde', 'array', 'begin', 'end']
prefix = 'a'
print(filter_by_prefix(strings, prefix))  # ['abc', 'array']
```
This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses the `startswith` method to achieve this.