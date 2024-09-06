```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string] + all_prefixes(string[1:])

def all_prefixes_test():
    input_str = 'abc'
    assert all_prefixes(input_str) == ['a', 'ab', 'abc'] + ['abc'] * 2
```