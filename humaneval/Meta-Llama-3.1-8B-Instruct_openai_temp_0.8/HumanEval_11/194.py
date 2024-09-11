```markdown
### Binary String XOR
#### Python Function to Perform Binary XOR on Two Binary Strings

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of XOR operation as binary string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for i, j in zip(a, b):
        # Use the XOR operator to get the result bit
        # and convert it to a string
        result += str(int(i) ^ int(j))

    # If the input strings have different lengths, 
    # XOR the remaining characters in the longer string with 0
    result += ''.join(str(int(i) ^ 0) for i in a[len(b):] if i!= '') or \
               ''.join(str(int(i) ^ 0) for i in b[len(a):] if i!= '')

    return result
```

### Example Usage

```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1111', '0000'))  # Output: '1111'
print(string_xor('1010', '1100'))  # Output: '0110'
```

Note: This function handles strings of different lengths by XORing the remaining characters in the longer string with 0.