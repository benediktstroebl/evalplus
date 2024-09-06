```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test the function with various inputs
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'cde'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['cde', 'array']
``` 
The function `filter_by_prefix` takes a list of strings and a prefix as input. It returns a option, which is a list of strings that start with the given prefix.