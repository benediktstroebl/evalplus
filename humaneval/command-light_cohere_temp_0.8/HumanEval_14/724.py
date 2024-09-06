Here is a Python script with a self-contained function that solves the problem of finding all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(p) for p in string if p]

# Test case:
def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

test()
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of its prefixes. The function uses a list comprehension and a condition to filter out prefixes from the input string.