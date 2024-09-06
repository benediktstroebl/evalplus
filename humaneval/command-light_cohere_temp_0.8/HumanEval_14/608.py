```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in string.
    # Test:
    assert all(all_prefixes('abc')) == ['a', 'ab', 'abc'],
    "All prefixes should be ['a', 'ab', 'abc']!"
```