```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    Parameters:
    a (str): Binary string consisting of 1s and 0s.
    b (str): Binary string consisting of 1s and 0s.
    
    Returns:
    str: Binary string consisting of 1s and 0s, result of binary XOR operation.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings have the same length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # Perform binary XOR operation
    result = ''
    for i in range(max_len):
        if a[i] == '1' or b[i] == '1':
            result += '1'
        else:
            result += '0'
    
    return result
```

You can use this function as shown in the example to perform binary XOR operation on two binary strings. The function first ensures both strings have the same length by padding the shorter string with leading zeros. It then performs the XOR operation by iterating over each character in the strings and appending '1' to the result if either character is '1', and '0' otherwise.