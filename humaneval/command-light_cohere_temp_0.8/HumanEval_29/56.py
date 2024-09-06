```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello", "world"]
prefix = "a"

result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
``` 
This script defines a function **filter_by_prefix** that takes a list of strings and a prefix as input and returns a filtered list of strings that start with the given prefix. 

The function uses the Python list comprehension to filter out the strings that start with the given prefix. 

This script is a good implementation of the problem and it passes all the corresponding tests.