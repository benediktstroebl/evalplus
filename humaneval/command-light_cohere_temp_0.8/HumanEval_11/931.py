```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    return ''.join(a^[i] ^ b^[i]) for i in range(len(a))
    """

tests = [
    "010" ^ "110" == "100",
    "0011" ^ "0110" == "1010",
    "1010" ^ "0011" == "1111",
    "0000" ^ "1111" == "1111",
    "130" ^ "411" == "361",
    "00111" ^ "00110" == "011010"
]

for test_str in tests:
    print(string_xor(*test_str)))
```