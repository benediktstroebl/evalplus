```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.full() if prefix != '']

# Test cases
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('xx') == []
    assert all_prefixes('') == []
    assert all_prefixes('  ') == ['']
    assert all_prefixes('123') == ['1', '23']
```
This script defines a function that returns a list of all prefixes from the shortest to the longest in a given string. It is designed with type hints and has corresponding test cases.