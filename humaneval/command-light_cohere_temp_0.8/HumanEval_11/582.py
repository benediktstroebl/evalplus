```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two input strings consisting only of 1s and 0s.
    return ''.join([a[i]^b[i] for i in range(len(a))])

# Example test cases
test_string_xor = [
    ("010", "110").apply(string_xor),
    ("001", "001").apply(string_xor),
    ("1010", "0110").apply(string_xor)
]

print(test_string_xor)
```