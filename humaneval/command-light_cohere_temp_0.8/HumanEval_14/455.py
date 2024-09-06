```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string(). important:  # String needs to be at least time
    return ['a' if c.isalpha(c) else c for c in string]

def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This code defines a function all_prefixes that returns a list of all prefixes in a given string. The test_all_prefixes function tests whether the result of all_prefixes is correct by asserting that the function correctly returns the list of prefixes from the string 'abc'.