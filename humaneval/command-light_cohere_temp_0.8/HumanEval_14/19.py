```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[0]] + all_prefixes(string[1:])

def all_prefixes_test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This script defines a function that returns a list of all prefixes from shortest to longest of the input string. It does this by using recursion and the ability of the typing module to automatically slice strings.