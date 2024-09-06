```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    Function performs binary XOR operation on two input strings consisting only of 1s and 0s and returns the result as a string.
    Args:
        a: str, string containing only 1s and 0s
        b: str, string containing only 1s and 0s
    Returns: str, The result of performing binary XOR operation on a and b
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
# Test case 1
print(string_xor('010', '110'))
# Test case 2
print(string_xor('111', '010'))
```
The above code defines a function called `string_xor` that performs a binary XOR operation on two input strings consisting only of ones and zeros. The function first checks if the string lengths are equal, and if not, it raises a ValueError. The function then iterates over the strings, performs a bitwise XOR operation on each corresponding character and appends the result to the `result` string. Finally, the function returns the string as the result.