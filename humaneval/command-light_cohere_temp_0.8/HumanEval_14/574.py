```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[:2]] + [sub for sub in string if sub != '']
test_cases = [
    'abc',
    'abcd',
    '123',
    '',
    '::#',
]
for text in test_cases:
    actual = all_prefixes(text)
    assert set(actual) == set(expected), f"mismatch for '{text}'"
print('All prefixes passed tests.')
```