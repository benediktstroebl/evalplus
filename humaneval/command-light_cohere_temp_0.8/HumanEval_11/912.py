```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of single characters.
    : Perform binary XOR operation and return result as a string.
    """
    `a = '010'
    `b = '110'
    return a^b  # return result

# Test cases
test_string_xor = []
test_string_xor.append(['010', '110', '100', '001', '1010'])

# Verify expected results
for test in test_string_xor:
    assert string_xor(test[0], test[1]) == test[2]
```