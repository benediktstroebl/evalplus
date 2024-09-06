```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # corresponding tests... Test cases:
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'ac', 'bc']
    assert all_prefixes('abcf') == ['ab', 'ac', 'cf']
    assert all_prefixes('abcde') == ['abc', 'abcd', 'ace']
    assert all_prefixes('') == []
```