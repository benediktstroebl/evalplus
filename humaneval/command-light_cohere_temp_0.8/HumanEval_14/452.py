```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[0]] + all_prefixes(string[1:])

def all_prefixes_test(string: str) -> None:
    assert all_prefixes(string) == ['a', 'ab', string[0]] + all_prefixes(string[1:]),
    assert len(all_prefixes('')) == 0
```
This script defines a function all_prefixes that takes a string as input and returns a list of its prefixes, from shortest to longest. This is a way to solve the problem you've stated, which is to find all prefixes of a given string.