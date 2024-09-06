```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of 1s and 0s.
    XOR is strings bit and b in their respective places
    XOR(a[0], b[1])
    XOR(a[1], b[0])
    ...
    """
    return ''.join(chr(a[i] ^ b[i]) for i in range(len(a)))
# Tests
a = "010"
b = "110"
print(string_xor(a, b)) # Output should be 100
print(string_xor("".join(), b)) # Input empty string, should return empty string
print(string_xor("".join(), "".join())) # All single character strings are empty
print(string_xor("".join() + ".".join())) # Concatenation of single characters, should be ['0','1','8']
print(string_xor("".join() + "".join())) # Concaten of single characters, should be ['1','8']
```
This function uses the XOR operation to return a new string where characters in a and b are XORed. The test cases cover various edge cases: empty input, all single character inputs, and concatenation of strings.