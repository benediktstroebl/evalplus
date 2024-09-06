```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```  This Python function, `filter_by_prefix`, filters an input list of strings and returns only those that start with a specific prefix. It uses the filtering technique, where it iterates through the input list and uses the `startswith` method to check if each string starts with the specified prefix.