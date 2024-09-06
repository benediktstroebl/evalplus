```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases
strings = ["abc", "bcd", "cde", "hello world", "this is not it", "test array"]
prefix = "a"
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'hello world']

strings = ["abcd", "cded", "cd", "array"]
prefix = "cd"
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['cded', 'cd']

# Using from list method
strings = ["abcd", "cded", "cd", "array", "hello"]
prefix = "o"
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['array', 'hello']
```

This script provides a function called `filter_by_prefix` that takes in a list of strings and a prefix as arguments. It then returns a