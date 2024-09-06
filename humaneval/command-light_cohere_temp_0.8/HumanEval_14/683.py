```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [s for s in string if s else '']
test_cases = [
    'abc', 
    'abcd', 
    'hello world', 
    '         ', 
    ''         ]
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab']
    assert all_prefixes('hello world') == ['hello']
    assert all_prefixes(' ') == ['']
    assert all_prefixes('test') == []
    assert all_prefixes('') == []
```
Do you want help with anything else?