```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test cases for function
test_strings = [ 'abc', 'bcd', 'cde', 'a', 'array', 'position' ]
test_prefix = 'a'

result = filter_by_prefix(test_strings, test_prefix)
print(result)  # Output: ['abc', 'array']
```

The code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It works by using a List[str] that returns all strings in the list, and the prefix parameter that specifies the prefix to match. The function uses the `startswith` function that checks if each string starts with the given prefix. The output is a list of strings that start with the specified prefix.