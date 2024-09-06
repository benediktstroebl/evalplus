```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR by performing the XOR operation on the corresponding bits of `a` and `b`. Here's a step-by-step explanation of the code:
1. The function `string_xor` takes two arguments `a` and `b`, which are of type `str` and are binary strings consisting of only 1s and 0s.
2. The return type of the `string_xor` function is also `str`, and it uses the `join` method to concatenate the characters returned by the loop.
3. The `zip` function takes two iterables (`a` and `b`) and returns a zip object. It pairs the corresponding elements of both iterables together, doing it element-by-element. In this case, it pairs the characters of `a` and `b` based on their positions.
4. For each pair of characters `(x, y)` returned by `zip(a, b)`, the script uses the `chr` function to convert the binary string to a decimal number, which is then fed to the `^` operator to perform the bitwise XOR operation `int(x) ^ int(y)`.
5. The `^` operator returns the binary string of the result of the XOR operation between the corresponding bits of `a` and `b`.
6. The `join` method concatenates all the XORed binary strings together to form the final result, which is then returned by the `string_xor` function.

This solution is concise and efficient, and it provides a clear way to perform binary XOR on two binary strings.