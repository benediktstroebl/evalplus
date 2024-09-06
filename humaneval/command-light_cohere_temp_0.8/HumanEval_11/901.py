```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings.
    # Input two strings a string
    # remove all non-alph digits from each
    # perform XOR
    result = ''.join(c if c in '01' else '0')
    return result

# Test case
test_suite = [
    '010', '110', '100',
    '001', '11', '10'
]

for test in test_suite:
    actual_xor = string_xor(test, test)
    assert actual_xor == test
```