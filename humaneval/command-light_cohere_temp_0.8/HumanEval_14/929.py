```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != '']

# Test cases
test_cases = [
    ('abc', ['a', 'ab', 'abc']),
    ('123', ['123']),
    ('abcdefgh', ['abcdef', 'abcdefgh']),
    ('', []),
    (' Rush Hour', [' Rush Hour '])
]

for text, expected in test_cases:
    actual = all_prefixes(text)
    assert actual == expected, f"Expected: {expected}, Got: {actual}"
```

This code defines a function that returns a list of prefixes from a given input string, it then passes various test cases to ensure the function's correctness. The test cases include strings with various lengths and characters, and the function correctly returns the expected prefixes.