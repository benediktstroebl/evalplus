```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests
strings = ['abc', 'bcd', 'cde', 'a', 'array', 'xx']
prefix = 'a'
test_strings = filter_by_prefix(strings, prefix)
print(test_strings)
# Prints ['abc', 'array']
```
This script defines a function `filter_by_prefix` that filters an input list of strings, returning only those that start with a given prefix. The function utilizes the test cases, where it creates a test list of strings and a corresponding prefix, then calls the function to filter the strings and prints the resulting list.