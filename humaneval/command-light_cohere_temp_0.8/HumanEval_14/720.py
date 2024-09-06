```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(s) for s in string.string() if s]
```
# tests
test_all_prefixes("abc")  # Output: ['a', 'ab', 'abc']
test_all_prefixes("x Hippolyte")  # Output: []
test_all_prefixes(" ")  # Output: []
test_all_prefixes('\n')  # Output: []
```