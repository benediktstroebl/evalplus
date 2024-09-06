```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [x for x in string if x != '' and x not in ['', ',']]

# Test case 1: Basic strings
test_cases = [
    'abc',
    '123',
    '',
    ' ',
    'abc123',
    'abc123_',
    'aa',
    '123 456',
    'abc123_abc'
]

for case in test_cases:
    assert all_prefixes(case) == ['a', 'ab', 'abc', '']
```
The provided Python script defines a function all_prefixes that returns a list of prefixes from the input string. It utilizes a simple criteria to identify prefixes: non-empty characters and exclude spaces and commas. The test cases cover various scenarios, including basic strings, numbers, empty strings, and strings with various separators.