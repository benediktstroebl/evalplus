```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only ones and zeros.
    return sum((x string.
    """ The pure function using only ASCII ones and zeros and applying XOR operator
    """
    return "".join(chr((a[i] ^ b[i]) if a[i] != b[i] else 0) for i in range(len(a)))

# Test cases
test_string_xor = ['010', '110', '00', '001', '0110', '1000']
test_cases = [
    ("".join(0),),
    ("".join(1),),
    ("".join("0"),
    ("".join(1), "0"),
    ("".join("0", "1"),
    ("".join("1", "0"))
]

# Test if the function is working correctly
for test_str, expected_result in test_cases:
    actual_result = string_xor(*test_str)
    print(f"Test: {test_str}, {actual_result}, expected_result)
```