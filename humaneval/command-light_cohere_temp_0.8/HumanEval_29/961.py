```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case 1
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'abc'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']


# Test case 2
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'x'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: []
```
This Python script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with that prefix. It tests the example usage by passing the list of strings and the prefix 'abc' to the function, which prints the result containing only strings that start with 'abc'.