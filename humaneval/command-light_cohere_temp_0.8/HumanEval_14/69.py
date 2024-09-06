```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != '']

# Test cases
test_cases = [
    'abc',
    'a',
    'ab',
    '123',
    '',
    'a ',
    '     ',
]

for test_str in test_cases:
    assert all_prefixes(test_str) == ['a', 'ab', 'abc']
``` 
The code defines a function called `all_prefixes` that takes a string `string` as input and returns a list of its prefixes. It uses a specific logic to filter out non-alph characters and create the corresponding list of prefixes.