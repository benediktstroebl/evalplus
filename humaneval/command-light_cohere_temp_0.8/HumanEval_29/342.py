```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "hello", "world", "!!!!!"]
prefix = "abc"

# Function Call
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'bcd', 'cde']
```

This code defines a function called `filter_by_prefix` that filters an input list of strings based on a given prefix. It uses the filtering technique to check if each string in the list starts with the specified prefix. The function then returns a filtered list.

The script also provides a test case with a list of strings and a specific prefix. It then calls the string with the test case, and prints the result, which should be the list of strings that start with the given prefix.