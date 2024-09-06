```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two binary strings, `a` and `b` as inputs. It uses `typing.zip` to iterate over corresponding characters from both strings, performs binary XOR on the corresponding characters using `^` operator, and converts the resulting binary strings to ASCII using `chr` function. The join method is then used to combine these characters into a string that is returned by the function. 

This function returns the binary XOR of the two input strings.