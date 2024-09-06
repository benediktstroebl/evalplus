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

This script defines a function `string_xor` that takes two strings `a` and `b` as binary strings (consisting of 1s and 0s) as input and performs a binary `xor`. The `xor` is carried out by iterating through each character of both strings and appending a `1` to the result if the characters differ in the two strings, and a `0` if they are the same. Lastly, the function returns this resultant string. 

Here is an example usage of this function:
```python
>>> string_xor('010', '110')
'100'
``` 
This example usage demonstrates the function's ability to correctly perform a binary `xor` on the two input strings '010' and '110', resulting in the desired output '100'. 

This function can be easily utilized anywhere where binary operations on binary strings are required.