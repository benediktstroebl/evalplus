```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Example test cases:
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'abc'

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```

This code defines a function called `filter_by_prefix` that takes two arguments: a list of strings `strings` and a prefix `prefix`. It uses a list comprehension to filter and return only the strings from the input list that start with the specified prefix.