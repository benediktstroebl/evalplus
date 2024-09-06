```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Unit tests
strings = ['abc', 'bcd', 'cde', 'array', 'xf', 'zab']
prefix = 'a'
test_strings = filter_by_prefix(strings, prefix)

print(test_strings)
 assert test_strings == ['abc', 'array']
 ```