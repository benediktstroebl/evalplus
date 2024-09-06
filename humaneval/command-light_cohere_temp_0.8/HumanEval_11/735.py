```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of digits 1 and 0.
    :return: String
    :args[a, b]
    """
    # Convert to list of characters to ensure ascii rules
    al = ''.join(a)
    bl = ''.join(b)
    result = ''.join([x ^ y for [x in '0'] != y in '0'] for x, y in zip(al, bl)])
    return result

# Test suite
test_suite = [
    ('010', '110'),
    ('100', '001'),
    ('001', '100'),
    ('110', '001'),
    # Add more tests as needed
]

for act, act_expected in test_suite:
    actual = string_xor(act, act)
    print(f"ACT: {act}, ACT_EXPECTED: {actual}, ERROR: ")
    print(f"{actual} != {act_expected}")
```