```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'
    return result
```

This script defines a function called `string_xor` that takes two strings `a` and `b` as input. It performs a binary XOR operation on these two strings and returns the result as a new string. The function checks each character of the two strings at the same index position and adds a '1' to the result string if the characters are different, and adds a '0' if the characters are the same. Overall, this function solves the problem of performing binary XOR on two strings of 1s and 0s and returns the result as a string.