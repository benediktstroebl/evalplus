```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "a1", "array", "beep"]
prefix = "a"

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```

This Python code defines a function called `filter_by_prefix` that filters an input list of strings based on a given prefix. It utilizes the filtering by checking if each string in the input list starts with the provided prefix. The function returns a filtered list of strings that match the given prefix.