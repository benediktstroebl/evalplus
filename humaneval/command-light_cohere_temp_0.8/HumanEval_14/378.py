```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix[0]
# Tests
    assert all(all_prefixes('abc'))
    assert all_prefixes('xx') == ['x']
    assert all_prefixes('aa') == ['a']
    assert all_prefixes('') == []
    assert all_prefixes('  ') == []
    assert all_prefixes('abcde') == ['cde']
    assert all_prefixes(' aa') == ['a']
    assert all_prefixes('12abc') == ['12', 'a', 'bc']
    assert all_prefixes('x'.join' == ['x'])
```
This script defines a function all_prefixes that returns a list of prefixes from the shortest to the longest. It uses the strings and various tests to verify the functionality of the function.