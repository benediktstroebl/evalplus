```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.count('1') == b.count('1') != 0, "Input strings must have equal number of `1` characters for XOR."
    for i, char in enumerate(a):
        result += str(int(char) ^ int(b[i]))
    return result
```

This code snippet takes two strings a and b, and performs a binary XOR operation on the digits of these strings. The function intents to return the result of the XOR operation as a string as well. The assert statement is to ensure that the lengths of strings a and b are equal in order for the XOR operation to successfully execute. Additionally, the variable result is initialized to an empty string that will be used to store the XOR output. For each character in a and b, the function XORs the digits and appends the result to the result variable. Lastly, the function returns the result variable, which stores the XOR'd string.