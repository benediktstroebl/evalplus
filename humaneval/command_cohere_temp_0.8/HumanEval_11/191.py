```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a) // 3)
```

The provided Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. This function performs a binary XOR operation on the bits of `a` and `b`. It achieves this by first converting the input strings to their respective binary integers using the `int(a, 2)` and `int(b, 2)` conversions. Then, it computes the bitwise XOR by taking the binary sum of these integers using the `^` operator. 

Finally, the function returns the result of the binary XOR operation as a string by converting the binary integer result back to a string format and padding it with leading zeros (using `.zfill(len(a) // 3)` to ensure the output length is similar to the input length) to maintain uniform length for identical-length inputs. 

The `string_xor` function serves to efficiently perform binary XOR on two strings consisting of binary digits (`0`s and `1`s) and provides a formatted output. It allows for bitwise manipulation of binary strings without the need for additional string manipulation techniques.