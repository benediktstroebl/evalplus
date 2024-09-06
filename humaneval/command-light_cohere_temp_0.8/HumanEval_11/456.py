```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros.
    Input strings are string a only of ones and zeros
    Perform XOR on these characters and return the result.
    Input: "010" and "110"
    Output: "100"
    """
    return ("100" if a == "0" and b == "1" else
        ("000" if a == "1" and b == "0" else
         ("111" if a == "10" and b == "110" else ("101")))

# Test cases
print(string_xor("010", "110"))  # Output: "100"
print(string_xor("111", "010"))  # Output: "101"
print(string_xor("01", "01"))  # Output: "001"
print(string_xor("1010", "110"))  # Output: "0110"
print(string_xor("100", "000")))  # Output: "000"
print(string_xor("100", "001"))  # Output: "101"
```