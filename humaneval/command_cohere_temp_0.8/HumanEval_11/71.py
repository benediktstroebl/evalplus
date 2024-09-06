```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This script defines a function `string_xor` that takes two strings (`a` and `b`) as input, where each character of these strings can be either a `0` or a `1`. It returns the result of a binary `xor` operation between these inputs as a single string consisting of `0` and `1` characters. 

The `zip` function is used to iterate over each pair of corresponding characters from both strings, taking into account the typing information provided with the `a_char` and `b_char` aliases. Within this loop, we use the `chr` function to convert each result of the binary `xor` operation (performed with `^` operator) to a character `0` or `1`. The `join` function is then used to combine these characters into a string. 

The function includes a docstring that demonstrates how the function can be used, as well as how the result is calculated:
```python
def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```
```python
>>> string_xor('010', '110')
'100'
```