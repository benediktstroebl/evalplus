```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix."""
    return [x for x in strings if x.startswith(prefix)]


# Test case 1: Basic function usage
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']

# Test case 2: List of strings with non-matching prefix
strings = ['abc', 'bcd', 'cde', 'hello', 'world']
prefix = 'xx'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: []

# Test case 3: Lists with mixed strings and non-matching prefix
strings = ['a', 'bc', 'd', 'hello', 'world']
prefix = 'xx'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: []
``` 
This Python script defines a function `filter_by_prefix` that takes two arguments: a list of strings and a prefix string. It then filters this strings in the list, keeping only the ones that start with the provided prefix. This script provides three basic function usage and demonstrates a problem of filtering strings based on a prefix, which can be useful for tasks like removing prefixes or tokens from a string.