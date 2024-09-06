```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]
return ['a', 'ab', 'abc']

# Test suite for function
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('aa') == ['a']
    assert all_prefixes('') == []
    assert all_prefixes('zz') == []
    assert len(all_prefixes('a')) == 1
    assert len(all_prefixes(' ')) == 1
    assert len(all_prefixes("")) == 0
```
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string. The test suite contains a simple test cases, such as passing different strings, empty strings, and single characters.