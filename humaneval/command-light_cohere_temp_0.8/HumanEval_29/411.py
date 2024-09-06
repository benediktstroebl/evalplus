```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Tests
strings = ['abc', 'bcd', 'cde', 'array', 'ez', ' welcome']
prefix = 'cde'

print('Test 1: ', end='')
print(filter_by_prefix(strings, prefix))
print('\n')

strings = ['aab', 'abcd', 'ace', 'act', 'aardvark']
prefix = 'act'

print('Test 2: ', end='')
print(filter_by_prefix(strings, prefix))
``` 
This code defines a function **filter_by_prefix** that filters an input list of strings and returns a new list containing only the strings that start with a specified prefix.  It then tests this strings and the corresponding prefix to pass to the function and prints the results.