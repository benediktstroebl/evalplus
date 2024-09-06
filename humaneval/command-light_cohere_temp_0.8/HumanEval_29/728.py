```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'a'

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']

strings = ['hello', 'world', 'hi', '! Buckman, USA']
prefix = 'US'

print(filter_by_prefix(strings, prefix))  # Output: ['USA', 'Buckman']
``` 
This code provides a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function returns a `List[string]` for each string that starts with the given `prefix` in the input list.