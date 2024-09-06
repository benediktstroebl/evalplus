```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.abc + string.split() if len(string) > 1]

# tests
def test_function(test_str): 
    assert all_prefixes(test_str) == ['a', 'ab', 'abc']
test_str = 'abc'
test_function(test_str)  # pass
```