```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Unit tests
test_filter_by_prefix = []
test_strings = ['abc', 'bcd', 'cde', 'array', 'hello']
test_prefix = 'a'
test_result = filter_by_prefix(test_strings, test_prefix)
test_filter_by_prefix.print(test_result)
print(test_result)  # Output: ['abc', 'array']
``` 
The function **`filter_by_prefix`** takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix. 
This is a self-contained function and does not require external modules or functions.