```python
import stringio
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    return "".join([x[ord == '1' or ord('0') for ord in a] ^ [ord == '1' or ord('0') for ord in b])

test_suite = [
    "input two strings consisting only of ones and zeros",
    "expecting result as a string",
    " Got: ",
    " xor('010', '110')",
    " should be: ",
    "100"
]

#test_suite
with stringio.write(string_xor.__code__, 'test_suite') as code:
    print(code.print('test_suite'))
```
This code defines a function called `string_xor`, which performs a bitwise XOR operation on two input strings containing only ones and zeros, and returns the result as a string. It also provides a test suite to verify the correctness of the `string_xor` function.