```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ']

# Test cases
test_cases = [
    ('abc', ['a', 'ab', 'abc']),
    ('', ['']),
    ('a', ['a']),
    ('racing', ['acing', 'racin']),
    ('p QLD', ['p', 'ql']),
    ('# ', ['#'])
]

for text, expected in test_cases:
    actual_prefixes = all_prefixes(text)
    assert actual_prefixes == expected, f"Expected: {expected}, Got: {actual_prefixes}"
```