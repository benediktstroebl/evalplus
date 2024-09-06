```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char for char in string if char.isalpha()) for i, 1, string.->split('') for i in range(len(string) + 1) if len(string) > 0]

def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
Do you need anything else I can assist you with?