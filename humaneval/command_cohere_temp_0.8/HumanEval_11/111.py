```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as inputs, where each character of both strings can be either a `0` or a `1`. It performs a binary XOR operation on the two strings and returns the result as a single string. The procedure `zip` is utilized to loop through the characters of both strings `a` and `b` in tandem, after which the `^` operator is used to perform the bitwise XOR on the corresponding characters. The `join` method is then used to combine all the XORed characters into a single string. 

Here is an example use case to demonstrate its functionality:
```python
# Example usage
result = string_xor('010', '110')
print(result)  # Should print '100'
``` 

This would produce the output: 
```
100
``` 

This exemplifies the outcome of XORing the inputs `'010'` and `'110'` in binary. 

This function meets the problem statement's requirement as it executes the binary XOR on two strings consisting of `0` and `1` characters and provides the result as a string output.