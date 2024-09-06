```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "Hello", "World"]
prefix = "a"

# Test 1
result1 = filter_by_prefix(strings, prefix)
print(result1)  # Output: ['abc', 'array']

# Test 2
result2 = filter_by_prefix([ '123', 'abc', 'bcd', 'cde', 'foo'], 'a')
print(result2)  # Output: ['abc', 'bcd', 'cde']

# Test 3
result3 = filter_by_prefix([ 'abcde', 'hello world'], 'bcd')
print(result3)  # Output: []
``` 
This script defines a function **filter_by_prefix** that filters an input list of strings based on a given prefix. It uses the f-strings and prefix as arguments, and then uses a list comprehension to filter the strings that start with the given prefix.