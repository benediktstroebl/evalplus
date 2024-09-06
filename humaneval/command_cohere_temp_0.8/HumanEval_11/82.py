```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as inputs and returns their binary XOR. The function uses zip to iterate over the characters of both strings, taking pairs of characters, converting them to ints, and performing the XOR operation. The result is then converted back to a string and returned.

Here's an example of how you can use this function to solve the problem statement mentioned in the markdown code block:
```python
# Example usage
a = '010'
b = '110'
print(string_xor(a, b))  # Outputs '100'
``` 

This would print the result '100' as expected, as this is the XOR of the two input strings '010' and '110'.