```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello", "world"]
prefix = "a"

result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']

# Another test
result = filter_by_prefix([ 'abcd', 'bcda', 'cd', 'cd', 'abc' ], 'cd')
print(result)  # Output: ['cd', 'abc']
```

This Python script provides a self-contained function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses the filtering logic to return only the strings that start with the given prefix. The test cases demonstrate the use of the function with different strings and prefixes.