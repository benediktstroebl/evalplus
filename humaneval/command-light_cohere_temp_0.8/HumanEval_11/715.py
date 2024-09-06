```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros
    """
    return a ^ b

# Testing the function with known correct results
tests = [
    ("010", "110" , "100"),
    ("01", "10" ,"100"),
    ("001", "001" , "110"),
    ("100", "001" , "01"),
    ("1010", "1110", "0000"),
    ("00", "1111", "1111")
]

for test in tests:
    print(string_xor(test[0], test[1]))
```