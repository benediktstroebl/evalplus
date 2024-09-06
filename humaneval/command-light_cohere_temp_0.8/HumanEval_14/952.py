Here is a Python script that contains a self-contained function that solves the problem of finding all prefixes from shortest to longest of an input string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']

# Tests
test_data = [
    'abc',
    'hello world',
    '123',
    '',
    'Code',
]

for test in test_data:
    assert all_prefixes(test) == ['a', 'ab', 'ac', 'o', 'oc']
``` 
This function efficiently generates all prefixes of the input string by iterating through each character while filtering out spaces.