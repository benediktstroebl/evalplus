```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != '']

# Test case: get all prefixes of "abc"
assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This code defines a function `all_prefixes` that returns a list of all prefixes of a given string. It uses list comprehension and a Python in the function body.