```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input, where each character can be either a '0' or a '1'. It performs a binary XOR operation on the two strings and returns the result as a single string. 

The script uses a list of tuples `zip(a, b)` to iterate over the corresponding characters of the input strings `a` and `b`, performing the XOR operation on the ASCII values of these characters and converting the result back to a character using `chr()`. Finally, it joins these characters together to form the output string.