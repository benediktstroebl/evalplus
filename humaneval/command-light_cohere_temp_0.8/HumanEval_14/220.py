```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[0]] + all_prefixes(string[1:])

def all_prefixes_test(string: str) -> None:
    assert all_prefixes(string) == ['a', 'ab', string[0]] + all_prefixes(string[1:]),
    assert len(all_prefixes(string)) == 3
```