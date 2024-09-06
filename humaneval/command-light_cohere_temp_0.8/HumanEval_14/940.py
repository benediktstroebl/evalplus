```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join() for i, char in enumerate(string, 1, 1)]

# Tests
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('xx'))  # []
print(all_prefixes('a'))   # ['a']
print(all_prefixes(''))    # []
```
The function uses a generator expression to iterate through each character of the string from the shortest possible prefix to the longest, and generates a list of prefixes. It tests by passing the