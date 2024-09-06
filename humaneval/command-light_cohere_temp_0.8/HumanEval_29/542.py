```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests
strings = ['abc', 'bcd', 'cde', '11', 'array', 'vegetation']
prefix = 'a'
test_strings = filter_by_prefix(strings, prefix)
print(test_strings)  # Output: ['abc', 'array']
test_strings = ['bcd', 'cde', 'abc', '11']
prefix = 'x'
test_strings = filter_by_prefix(strings, prefix)
print(test_strings)  # Output: []
``` 
This code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. The function returns a string that starts with the given prefix. 

The output of the code is the list of strings that start with the given prefix.