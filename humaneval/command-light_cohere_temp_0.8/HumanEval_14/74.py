```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.py.lower() for string.split('.') if '.'.  #else the other 

# tests
def test_all_prefixes(test_str: str) -> None:
    assert all_prefixes(test_str) == ['a', 'ab', 'ac']
    return

test_str = 'abc'
test_all_prefixes(test_str)
print("Tests passed!")
```