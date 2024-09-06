Here is a self-contained Python script with a function that filters an input list of strings based on their prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello", "world"]
prefix = "a"
result = filter_by_prefix(strings, prefix)
print(result)

```

The code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with the specified prefix. The test cases demonstrate the