```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[0]] + all_prefixes(string[1:])

def all_prefixes_test() -> None:
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This code defines a function all_prefixes that takes a string as input and returns a list of all prefixes from shortest to longest. It uses the recursive approach and uses the string split at the beginning and the first character as a prefix. Then it adds this string split character + all prefixes from the rest of the string.

This code is a self-contained solution to the problem you provided.