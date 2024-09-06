```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as inputs. It uses `typing.zip` to iterate over the characters of both strings, performing binary XOR on the corresponding characters using `chr(int(x) ^ int(y))`. The result is then joined into a single string and returned.

Here is an example of how to use this function:
```python
# Test the function
assert string_xor('010', '110') == '100'
``` 

This will verify the function's behavior against the provided test case. Feel free to experiment with other inputs and assertions as needed.  If you want to test more cases, you can add additional assertions within the same test block. Here's an example:
```python
# Test the function with more cases
assert string_xor('001', '110') == '010'
assert string_xor('0111', '1000') == '001'
assert string_xor('1010', '0110') == '000'
``` 
This will cover more scenarios and ensure the function works correctly for various inputs.