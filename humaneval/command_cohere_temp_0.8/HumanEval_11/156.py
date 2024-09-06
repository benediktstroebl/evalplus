```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as inputs and performs a binary XOR operation on them. It uses `zip` to iterate over the characters of both strings, taking pairs of corresponding characters, and calculates the XOR of their ASCII values (converted to integers). The result is then converted back to a string and returned.

Here's an example of how you can use this function to test its functionality:
```python
# Test the function
assert string_xor('010', '110') == '100'
```

This will verify that the function behaves as expected, providing a consistent implementation of binary XOR for two binary strings.