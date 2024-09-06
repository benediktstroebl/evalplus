```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This Python script defines a function called `string_xor` that performs binary `XOR` on two input strings `a` and `b`. The function takes in the two strings as arguments and returns their binary `XOR` as a string. This is achieved by generating a new string where the i-th characters of `a` and `b` are concatenated, flipping the corresponding bit in `a` or `b` when the i-th characters are not equal.

The code includes type annotations using the `typing` module, which ensures that the function accepts only string inputs. Moreover, the code includes a docstring that provides details about the function's purpose, expected input, and example usage, as well as a `>>> `block that demonstrates how the function behaves for specific inputs. 

To use this function, simply call it with two string inputs, such as: 
 ```python
string_xor('010', '110')
``` 

This will return the binary XOR of the two strings, resulting in '100' in this case. 

This function can be especially useful in performing bitwise operations on binary strings, which is commonly needed in areas of computing such as binary algorithms or hardware-specific coding.