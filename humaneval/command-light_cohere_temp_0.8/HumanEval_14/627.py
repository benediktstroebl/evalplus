```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c.isalpha()]
```
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'ac', 'bd']
    assert all_prefixes('') == []
    assert all_prefixes('xx') == []
    assert all_prefixes('abcbb') == ['abc']
    assert all_prefixes(' 376') == ['36', '37', '76']

# Call the test suite.
test_all_prefixes() 
```