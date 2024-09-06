Here is a Python script that defines a self-contained function that solves the problem of XORing two strings:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Takes two strings consisting only of 1s and 0s and returns their XOR.

    if len(a) != len(b):
        return 'Invalid input lengths'

    xored = ''.join([c ^ d for d in b])
    return xored

# Example usage:
input1 = '010'
input2 = '110'
result = string_xor(input1, input2)
print(result)  # Output: 100
```
This solution follows the problem statement, which asks to perform the XOR operation on two strings with only 1s and 0s. The function handles the string lengths with an if statement, and performs the XOR operation on the first input string's character and the corresponding character from the second input string. The output is then the XOR of the two strings.