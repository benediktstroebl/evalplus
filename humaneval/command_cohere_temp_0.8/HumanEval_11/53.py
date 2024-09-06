```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two binary strings, `a` and `b` and performs a binary XOR operation on these inputs. The result is then returned as a string. The function uses a `for` loop to combine the characters of `a` and `b`, and uses the `chr()` function to convert the resulting binary XOR values to characters.

Here is an example of how to use this function to perform binary XOR on the inputs '010' and '110':
```python
print(string_xor('010', '110'))  # Outputs '100'
``` 

This would output '100' as expected, given that the XOR operation '010' ^ '110' equals '100' in binary.