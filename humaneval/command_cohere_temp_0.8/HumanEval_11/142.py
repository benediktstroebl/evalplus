```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
   Carry = False # Variable to store the carry Flag
    for i in range(min(len(a), len(b))):
        val = int(a[i]) ^ int(b[i])
        if val > 1:
            carry = 1
        else:
            carry = 0
        result = result + str(val)
        Carry = Carry ^ carry
    if Carry:
        result = result + '1'
    return result
```

The script uses bitwise XOR operation, operating on each corresponding character of the two input strings, with the Carry flag to handle the case when the result of XOR is 1. Then the function loops through the min of the lengths of the two strings, and returns the result.