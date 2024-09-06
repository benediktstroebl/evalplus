```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != ' ', 'a', 'b', 'c']

# Test the function with various inputs
test_cases = [
    ('abc', ['a', 'ab', 'abc']),
    ('abcde', ['abc', 'abcd', 'acde']),
    ('abc', ['a', 'ab', 'abc']),
    ('a','b','c'),
    ('#####', ['', ' ', '']),
    ('''', ['', '']),
    # Long strings for testing various boundary conditions
    ('a' * 1000, ['']),
    ('a' * 1000, ['a'])
]

for text, expected in test_cases:
    print(text, "Expected:",', expected)
    print(all_prefixes(text), "Actual:",,", sep=" -> ")
    assert all_prefixes(text) == expected
```