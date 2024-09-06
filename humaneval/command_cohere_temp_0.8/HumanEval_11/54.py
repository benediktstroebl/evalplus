```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as binary inputs (consisting of 1s and 0s) and performs a binary XOR operation on them. It uses `typing` for type hinting and uses `zip` to iterate over the corresponding digits of both strings, performing the XOR operation using `^` exponentiation operator. The result is then converted back to a string and returned.

Here's an example of how you can use this function to test its functionality:
```python
# Test the function
assert string_xor('010', '110') == '100'
```

This will verify the example scenario provided in the docstring, testing if the function behaves as expected.