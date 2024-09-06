```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Unit tests
strings = ['abc', 'bcd', 'cde', 'array', 'begin', 'end', 'hello']
prefix = 'a'
test_strings = filter_by_prefix(strings, prefix)
print(test_strings)  # Output: ['abc', 'array']
``` 
This Python code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. The function returns a filter the list of strings that start with the specified prefix. 

The code also includes unit tests, which create a separate strings list with various string elements and a specific prefix. This ensures that the test_strings list is correctly returned by the `filter_by_prefix` function with the specified prefix.