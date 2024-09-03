```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' if c.isalpha() else 'ab' else c for c in string]

# Test cases
string1 = "abc"
string2 = ""
string3 = "dEFgHijABC"
string4 = "#12345"

assert all_prefixes(string1) == ['a', 'ab', 'abc']
assert all_prefixes(string2) == []
assert all_prefixes(string3) == ['a', 'abc']
assert all_prefixes(string4) == ['#']

print("All prefixes passed tests!")
```