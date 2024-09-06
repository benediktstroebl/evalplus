```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings consisting of only 1s and 0s
    Returns: string_xor(input_str1, input_str2) 
    """
    return "".join(chr(i ^ j) for i, j in zip(a, b))
input_str1 = '010'
input_str2 = '110'
result = string_xor(input_str1, input_str2)
print(result) # Output: 100
```