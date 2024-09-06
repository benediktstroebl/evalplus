```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test case: Filter strings starting with 'a'
test_strings = ['abc', 'bcd', 'cde', 'array', 'begin']
test_result = filter_by_prefix(test_strings, 'a')
assert test_result == ['abc', 'array']
```

This script defines a function called **filter_by_prefix** that takes a list of strings and a prefix as input and returns a new list of strings that start with that given prefix. It is a simple and efficient way to solve the problem of filtering strings based on a prefix.