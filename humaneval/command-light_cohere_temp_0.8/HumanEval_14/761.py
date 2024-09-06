```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string() if prefix != '']

def test_function(string):
    assert all_prefixes(string) == ['a', 'ab', 'abc'], "Failed test: expected ['a', 'ab', 'abc'] but got %s" % string
    return

# Test the function
test_function('abc')
```