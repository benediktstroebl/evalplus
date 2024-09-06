```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
test_strings = ['abc', 'bcd', 'cde', 'a', 'heee', 'hello']
test_prefix = 'a'

result = filter_by_prefix(test_strings, test_prefix)
print(result)  # Output: ['abc', 'a', 'heee', 'hello']

``` 
This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. 

The function uses the `startswith` method to filter the strings by their prefixes.