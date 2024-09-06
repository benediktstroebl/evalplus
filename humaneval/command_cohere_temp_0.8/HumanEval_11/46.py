```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a) // 3)
```

The provided Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. This function performs a binary XOR operation on the bits of `a` and `b`. This operation is carried out by converting the input strings to their binary integer representations, performing the XOR operation on these integers, and then converting the result back to a string. The returned string represents the binary XOR of the two input strings.

Here is an example usage of this function:
```python
>>> string_xor('010', '110')
'100'
```

This will return '100' as the result of the binary XOR operation of the inputs '010' and '110'.