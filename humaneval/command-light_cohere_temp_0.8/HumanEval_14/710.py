```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[:2]] + [w for w in string if w != ' ' and w.tips() : 1]
```

def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('') == []
    assert all_prefixes('x') == ['x']
    assert all_prefixes('abcd') == ['ab', 'bc', 'cd']
    assert all_prefixes('abcde') == ['ab', 'ac', 'bcde']

# Run the function and test it
test_all_prefixes()
```