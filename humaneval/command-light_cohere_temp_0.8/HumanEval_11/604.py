```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Binary XOR operation between two strings"""
    return ''.join(c ^ ord(b[i]) for i,c in enumerate(a))

# Test suite for the function
test_string_xor = []
test_suite = [
    "string_xor('010', '110') -> '100'",
    "string_xor('00110', '01001') -> 100010",
    "string_xor('100', '01001') -> 00110",
    "string_xor('01001', '110') -> 001010",
    "string_xor('00101', '01001') -> 1000010",
]

# Run the function and test suite
for test in test_suite:
    print(test)
    result = string_xor(*test)
    assert result == test[1], "Test {} failed".
```