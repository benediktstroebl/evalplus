```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join() for i, char in enumerate(string, 1) if char != ' ' and i != 0]

# Test cases
test_cases = [
    ('abc', ['a', 'ab', 'abc']),
    ('abcde', ['abc', 'abcd', 'abcde']),
    ('123', ['1', '12', '123']),
    ('', [])
]

for text, expected in test_cases:
    actual = all_prefixes(text)
    assert actual == expected, f"Expected {expected}, but got {actual} for input: {text}"
```
This script defines a function all_prefixes that returns a list of all prefixes of a given string, it uses the enumerate function with start=1 and filters out spaces.  The also includes a test cases to ensure the function is working correctly for different inputs.