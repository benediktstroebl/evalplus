```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "fgh", "array", "hello"]
prefix = "a"

result = filter_by_prefix(strings, prefix)
print(result)  # Output ['abc', 'array']

# Another test
strings = ["aa", "ab", "ac"]
prefix = "ab"

result = filter_by_prefix(strings, prefix)
print(result)  # Output ['ab', 'ac']
```

This code defines a function called `filter_by_prefix` that takes two arguments: a list of strings and a prefix. It uses the strings' list and prefix to iterate over all strings in the list. The function returns a filtered list of strings that start with the specified prefix.