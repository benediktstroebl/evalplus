```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings containing only digits 1 and 0.
    The input is a and b, and return the result as a string.
    """
    # Convert inputs to lists of digits
    a = [c for c in a if c == '0']
    b = [c for c in b if c == '0']

    # XOR operation
    result = '0'
    for a_digit, b_digit in zip(a, b):
        result = (result << 1) | int(a_digit ^ b_digit)
    return result
```