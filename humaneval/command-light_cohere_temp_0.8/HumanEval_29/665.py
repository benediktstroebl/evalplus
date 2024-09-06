```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests
strings = ["abc", "bcd", "cde", "array", "Hello"]
prefix = "a"

# Test 1
assertEqual(filter_by_prefix(strings, prefix), ['abc', "array"]) )

# Test 2
assertEqual(filter_by_prefix([ 'abc', 'a' , "ccd'], prefix), ['abc'])

# Test 3
assertEqual(filter_by_prefix([ 'a', 'aa', 'b', 'bee', 'ccd'], prefix), ['a', 'aa', 'b'])
```
This script defines a function **filter_by_prefix** that takes in a list of strings and a prefix, and returns a new list that contains only the strings that start with the given prefix. The script also provides several tests to verify that the function works as expected.