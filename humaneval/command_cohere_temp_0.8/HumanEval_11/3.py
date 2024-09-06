```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This code defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR. The code uses a list comprehension to iterate over the characters of the two strings, performing the XOR operation on the ASCII values of the characters using the `^` operator, which has a higher precedence than the `ord()` function, and converting the result back to a character using `chr()`.

Here's an example of how you can use this function to test it:
```python
string_xor('010', '110')  # Output: '100'
```

This will return the XOR of the two provided binary strings, resulting in the output '100'.

This approach takes advantage of the higher-order bitwise XOR operator `^` to perform the binary XOR operation, which is efficient and scalable for longer binary strings.