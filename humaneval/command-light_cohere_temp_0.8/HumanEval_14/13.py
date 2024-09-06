```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ['a' if i < len(string) else '' for i in range(len(string))]

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("abcd", ["ab", "bc", "cd"]),
    ("", []),
    ("123", ["1", "12", "123"]),
]

for string, expected in test_cases:
    actual = all_prefixes(string)
    assert actual == expected
```