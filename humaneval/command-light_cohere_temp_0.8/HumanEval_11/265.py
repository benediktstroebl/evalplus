```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform XOR on two strings.
    a = a[a, '0', b]
    return ''.join(a[i] ^ b[i] for i in range(len(a)))

# Example usage
test_cases = [
    "010", "110", "100", "001", "1010", "1011"
]

for tc, expect in test_cases:
    print(f"Test case {tc}\n:")
    got = string_xor(tc, tc)
    print(f"Expected: {expect}\nGot: {got}")
    print()
``` 
The function uses the bitwise XOR operation (^) to return a string containing the XOR of the two input strings.