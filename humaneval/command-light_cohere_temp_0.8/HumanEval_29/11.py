```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'a'
expected = ['abc', 'array']

print(filter_by_prefix(strings, prefix))
print(expected)

strings = ['abc', '123']
prefix = 'a'
expected = ['abc']

print(filter_by_prefix(strings, prefix))
print(expected)
```

This script defines a function called **filter_by_prefix** that filters a list of strings based on a given prefix. It returns a the required input strings that start with the specified prefix. The script provides test cases that demonstrate the function's behavior correctly.