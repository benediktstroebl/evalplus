```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.py.uname_split(string) if prefix not in string]
# tests
test_string = "abc"
assertEqual(all_prefixes(test_string), ['a', 'ab', 'abc'])
```