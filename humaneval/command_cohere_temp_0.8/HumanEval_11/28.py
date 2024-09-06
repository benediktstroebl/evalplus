```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.replace('1', '0').replace('0', '1') == b, "Input strings must consist only of 1s and 0s."
    
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'
    return result
```

This function takes two strings a and b, performs binary XOR on them, and returns the result as a string. It utilizes bitwise XOR to simultaneously determine the appropriate '1' and '0' values in the result based on whether the corresponding bits of the input strings are different. This solution has a time complexity of O(min(n, m)), where n and m are the lengths of the input strings.