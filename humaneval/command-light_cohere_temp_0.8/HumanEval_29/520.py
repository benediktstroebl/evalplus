```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test cases for the function
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"
result = filter_by_prefix(strings, prefix)
print(result)
```