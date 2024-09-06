```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string] + all_prefixes(string[1:])
def all_prefixes_test() -> None:
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'ac', 'cd']
    assert all_prefixes('ab') == ['ab']
    assert all_prefixes('xx') == ['x', 'xx']
    assert len(all_prefixes('')) == 0
```