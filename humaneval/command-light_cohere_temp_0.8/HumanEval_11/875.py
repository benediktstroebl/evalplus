```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting only of 1s and 0s
    """
    # Perform binary XOR on the two input strings a and b
    return ''.join(chr((ord(a[i]) ^ ord(b[i]))) for i in range(len(a)))

# Test case: XOR '010' and '110'
assertEqual('100', string_xor('010', '110'))

# Test case: XOR '111' and '011'
assertEqual('111', string_xor('111', '011'))

# Test case: XOR '000' and '111'
assertEqual('111', string_xor('000', '111'))

# Test case: XOR '1010' and '1011'
assertEqual('1101', string_xor('1010', '1011'))

# Test case: XOR '1000' and '0111'
assertEqual('111', string_xor('1000', '0111'))
```

The function performs a binary XOR operation on two input strings, which only contain characters that are either '1' or '0'. The result is then returned as a string.