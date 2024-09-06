```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases for the filter_by_prefix function
strings = ["abc", "bcd", "cde", "a", "array", "bits"]
prefix = "a"

# Expected output
print(filter_by_prefix(strings, prefix))  # ['abc', 'a']
```