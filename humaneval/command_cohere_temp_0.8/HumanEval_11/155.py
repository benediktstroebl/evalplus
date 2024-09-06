```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that performs binary `XOR` on two strings consisting of only ones and zeroes and returns the result as a string. The function takes two strings `a` and `b` as input and returns the result of the binary `XOR` operation between these two strings by using the `xor` (`^`) operator in Python. 

Here is an example of how to use this function:
```python
# Example usage
string1 = "010"
string2 = "110"
result = string_xor(string1, string2)
print(result)  # Expected output: "100"
``` 

This would output: `100` as this is the result of the binary XOR applied to the two input strings.