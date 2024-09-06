```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.json.split() if any f(string)[:-1]]

# Test case:
test_string = "abc"
assert all_prefixes(test_string) == ['a', 'ab', 'abc']
```