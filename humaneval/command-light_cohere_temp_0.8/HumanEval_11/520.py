```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings containing only digits 1 and 0, and return result as a string.
    """
    operation = 0
    for i, c in enumerate(a):
        if c != '0': operation ^= c
    for i, c in enumerate(b):
        if c != '0': operation ^= c
    return str(operation)

# Test case 1:
print(string_xor('010', '110'))
# Expected output: 100

# Test case 2:
print(string_xor('YES', '0NO'))
# Expected output: differ
```

This Python script defines a function `string_xor` that performs the XOR operation on two input strings containing only the digit 1 or 0. The function uses a typing convention for better readability, and also creates a self-contained function with the `test case` included.