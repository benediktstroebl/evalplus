```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string. string() if x not a str[0]]

def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
```
This script defines a function all_prefixes that returns a list of prefixes from the shortest to the longest. The function uses a itertools.test_all_prefixes defines a function that tests whether the all_prefixes function correctly returns the expected output.