```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]

def test_function(string):
    return all_prefixes(string) == ['a', 'ab', 'ac']
```