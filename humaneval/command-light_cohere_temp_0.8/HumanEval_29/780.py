```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test cases
strings = ["abc", "bcd", "cde", "hello", "World"]
prefix = "array"

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']

strings = ["hello", "world"]
prefix = " abc"

print(filter_by_prefix(strings, prefix))  # Output: ['hello']
```
This script defines a function **filter_by_prefix** that filters a list of strings based on their prefix. The function uses the string starts with the given prefix.