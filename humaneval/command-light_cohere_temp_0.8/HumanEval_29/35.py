```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Test cases for the function
strings = ['abc', 'bcd', 'cde', 'first', 'array', 'number']
prefix = 'first'

print("Test 1 results: ", end="")
print(filter_by_prefix(strings, prefix))
print("\n")

strings = ['aab', 'acd', 'bb', 'first', 'array', 'number']
prefix = 'ab'

print("Test 2 results: ", end="")
print(filter_by_prefix(strings, prefix))
print("\n")
```
This script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It uses the basic Python list comprehension and the `startswith` method. The function is then tested using two sets of strings and passes the tests.