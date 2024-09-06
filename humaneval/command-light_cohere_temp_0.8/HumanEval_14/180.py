```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.py.asr(string)[:1]]

# Test cases
tests = [
    ('abc', ['a', 'ab', 'abc']),
    ('d', ['d']),
    ('', []),
    ('elixir', ['el', 'xi', 'xir'])
]

for test in tests:
    assert all_prefixes(test[0]) == test[1]
```