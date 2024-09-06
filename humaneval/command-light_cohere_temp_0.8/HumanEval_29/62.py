```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'for', 'true']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
``` 
This Python script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. It returns a The filtered list containing strings that start with the specified prefix. 

This script is self-contained and will print the expected output when you run it.