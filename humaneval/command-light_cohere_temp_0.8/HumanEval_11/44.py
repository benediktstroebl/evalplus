```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only ones and zeros.
    return ''.join(a.join(b))
``` 
# Test cases.
tests = [
    ("010", "110"),
    ("001", "010"),
    ("01", "100"),
    ("0000", "0000"),
    ("1010", "1111")
]

for a, b in tests:
    result = string_xor(a, b)
    print(f"Result: {result} - {a}, b = {a}, {b}")
``` 
The function string_xor in this script takes two strings a and b as inputs and returns the result of the XOR operation between them. The function joins the use the strings. The inputs are converted to lists of characters to simplify the code and improve readability. The output of the function is then printed to the console.