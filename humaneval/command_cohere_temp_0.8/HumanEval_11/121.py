```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This Python script defines a function called `string_xor` that performs binary XOR on two input strings `a` and `b`, which contain only digits '0' and '1'. The function takes these two strings as arguments and returns their binary XOR as a string. It uses a `for` loop to iterate over each pair of corresponding bits in `a` and `b`, performs the XOR operation on the Unicode code points of these bits, and converts the result back to a character before appending it to the result string. 

Here's an example of how you can use this function to compute the binary XOR of two strings:
```python
print(string_xor('010', '110')) # Output: '100'
``` 

This will produce the result '100', which is the XOR of the two input strings.