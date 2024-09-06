```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]

def test_function(string: str) -> None:
    actual_prefixes = all_prefixes(string)
    expected_prefixes = ['a', 'ab', 'abc']
    assert actual_prefixes == expected_prefixes
```