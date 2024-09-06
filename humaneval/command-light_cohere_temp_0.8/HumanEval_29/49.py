```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Testing the filter_by_prefix function
strings = ['abc', 'bcd', 'cde', 'array', 'html', '!' ]
prefix = 'a'

print("Filtered strings: ", filter_by_prefix(strings, prefix))

print("Prefix not found:", filter_by_prefix(strings, 'bcd' ))

print("All strings:", filter_by_prefix(strings))
```