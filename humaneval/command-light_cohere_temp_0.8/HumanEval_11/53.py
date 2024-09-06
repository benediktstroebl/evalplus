```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    """
    for char in range(min(len(a)), max(len(a))):
        if a[char] == '0' and b[char] == '1':
            return '0'
        elif a[char] == '1' and b[char] == '0':
            return '0'
        elif a[char] == '1' and b[char] == '1':
            return '1'
        else:
            return '10'
    return '11'
# Example usage
print(string_xor('010', '110'))  # Output: 100
```
This function performs a bitwise XOR operation on two strings consisting only of '0's and '1'. It uses a loop to iterate over each character in the input strings and performs the XOR operation accordingly. The output will the value '11' which corresponds to the XOR operation of the input strings.