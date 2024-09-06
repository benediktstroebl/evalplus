```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This Python script defines a function called `string_xor` that takes two binary strings, `a` and `b` as inputs. It uses `typing.zip` to iterate over corresponding characters from both strings, performing binary XOR through `^` operator and converting the result back to characters using `chr` and appending these characters to a blank string, `''`. 

The script returns the XORed result as a string. Test cases are not displayed in this rendition but the function should be capable of handling tests of different combinations of 1s and 0s in strings of varying lengths.