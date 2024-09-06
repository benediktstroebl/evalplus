```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # Test cases
    string length is a tuple of a single character
    # because it should not matter if the character is in a prefix,
    # or after the string, and also, the empty string should be treated as a single character
    # as well.
    test_cases = [
        ('', ()),
        (', ()),
        ('a', ''),
        ('ab', 'a'),
        ('abc', 'a'),
        ('a', 'ab'),
        ('ab', 'ab'),
        ('abcd', 'ab'),
        ('abcde', 'ab'),
        ('abcdef', 'ab'),
        ('a', 'abc'),
        ('abcda', 'abc'),
        ('abc', 'abcde'),
        ('ab', 'abcdeab')
    ]
```