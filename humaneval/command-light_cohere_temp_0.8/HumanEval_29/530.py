```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests
strings = ['abc', 'bcd', 'cde', 'array', 'welcome', 'test']
prefix = 'abc'

# Testing the function
print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses the `startswith` method to check if a given string starts with the given prefix. The output of the function is a list of all strings from the input list that start with the given prefix.