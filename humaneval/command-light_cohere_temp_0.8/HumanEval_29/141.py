Here is a Python script that contains a self-contained function that filters out strings starting with a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test the function with a sample input
test_strings = ['abc', 'bcd', 'cde', 'array', 'hello']
test_prefix = 'a'
filtered_strings = filter_by_prefix(test_strings, test_prefix)
print(filtered_strings)  # Output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that filters an input list of strings by removing those that do not start with the given prefix. It is then passes this tests using a sample input and prefix, and the function successfully filters the strings as expected.