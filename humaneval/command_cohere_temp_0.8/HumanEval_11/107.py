```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bytes.fromhex(a.translate(str.maketrans('01', '10')) ^ b.translate(str.maketrans('01', '10')))[0].decode()
```

This approach utilizes the translation method to convert strings consisting of 1s and 0s into hexadecimal bytes representation, and then performs XOR operation on those hex bytes using python's bitXor. The result is then returned to a string format.

The `translate` method is used to convert strings consisting only of 1s and 0s into their hexadecimal representation, and vice versa. This is achieved by defining a translation map with '01' as the input and '10' as the output.

The resulting hexadecimal strings are then fed to the `bitXor` function to perform the binary XOR operation.

The function returns the resulting string after performing binary XOR on the input strings.