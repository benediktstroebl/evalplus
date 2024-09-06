```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
```

This Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. It performs a binary XOR operation on these two strings and returns the result as a string. The function uses a for loop to iterate through the characters of the two strings, converting them to integers for the bit-wise XOR operation, and then converting the result back to a string to build the output.

Here's an example usage of the function:
```python
>>> string_xor('010', '110')
'100'
```

This would return "100" as the result of the binary XOR operation.