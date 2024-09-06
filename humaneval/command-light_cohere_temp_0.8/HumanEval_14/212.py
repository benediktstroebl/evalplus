```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join()[i:]+string for i, string in enumerate(string, 1)]

# Tests
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This script defines a function that returns a list of all prefixes of a given string, which is then tested with the test_all_prefixes function.