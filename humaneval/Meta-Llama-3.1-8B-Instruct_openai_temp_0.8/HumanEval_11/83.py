Here's a Python script that defines a function `string_xor` to perform binary XOR on input strings consisting only of 1s and 0s:
```markdown
### Binary XOR on Strings of Binary Digits
#### Problem: Perform binary XOR on two input strings consisting only of 1s and 0s.

```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First input string.
        b (str): Second input string.

    Returns:
        str: Result of binary XOR operation on a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR on the current characters from a and b
        # 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1, 0 ^ 0 = 0
        xor_result = str(int(char_a) ^ int(char_b))
        result += xor_result

    # If the input strings have different lengths, append the remaining characters from the longer string
    if len(a) > len(b):
        result += a[len(b):]
    elif len(b) > len(a):
        result += b[len(a):]

    return result
```

### Example Usage:

```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('1010', '1100'))  # Output: '0110'
```

### Note:

*   This script assumes that the input strings consist only of 1s and 0s.
*   If the input strings have different lengths, the script appends the remaining characters from the longer string to the result.