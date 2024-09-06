```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    : return list of strings with the given prefix
    """
    return [string for string in strings if string. starts with with prefix]

# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```

This code defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses the filtering technique where it iterates over each string and checks if the string starts with the provided prefix. It returns a list of strings with the given prefix.