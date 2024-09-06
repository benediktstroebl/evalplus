Here is a Python script that contains a self-contained function that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Example usage:
strings = ['abc', 'bcd', 'cde', 'array', 'function', 'good']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```
This script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses the method of taking a list of strings and a prefix, and then returns a new list that contains only the strings that start with that given prefix.