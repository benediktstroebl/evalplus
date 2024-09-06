```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [i for i in string if i != "" and i not in string[:-len(string)]]

# Tests
string1 = "abc"
string2 = ""
string3 = "aaaaaa"

assert all_prefixes(string1) == ['a', 'ab', 'abc']
assert all_prefixes(string2) == []
assert all_prefixes(string3) == ['aaaaaa']
```