```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases for the function
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'a'

# Check if the function correctly returns strings that start with the given prefix
print(f'filter_by_prefix(strings, prefix)': [{x: x[0] for x in strings if x.startswith(prefix)}')
# ['abc', 'hello']

# Check if the filter works with a non-existing prefix
print(f'filter_by_prefix(strings, 'x'): []
```