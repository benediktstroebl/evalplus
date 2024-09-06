```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Test cases
strings = ['abc', 'bcd', 'cde', 'a', 'array', 'phones', 'butterfly']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```
The code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with the given prefix. The test cases demonstrate the use of the function with various strings and prefixes. The output will be a list of strings that start with the given prefix.