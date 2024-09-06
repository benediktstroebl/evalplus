```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in string.
    # tests the identifier: all_prefixes()
    # tests
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'ac', 'bd']
    assert all_prefixes('abebceef') == ['ab', 'be', 'cef']
    assert all_prefixes('') == []
    assert all_prefixes(' ') == ['']
```
Do you have everything you need to solve the given problem?