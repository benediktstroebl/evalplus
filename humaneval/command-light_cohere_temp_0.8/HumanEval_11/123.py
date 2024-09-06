```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, a and b. both consisting of only ones or
    strings, and return the result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return '\n'.join([str(chr(x ^ y)) for x, y in zip(['01' + i] for i in a + b)])

# Test cases
tests = [
    ('010', '110'),
    ('001', '010'),
    ('001', '110'),
    ('110', '001'),
    # ... add more test cases ...
]

# Test function
def test(f: function) -> None:
    for a, b in tests:
        assert f(a, b) == str(chr(sum(map('01' + i for i in a + b))))

test(string_xor)
```