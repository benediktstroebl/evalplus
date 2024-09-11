```markdown
### Binary String XOR

This script performs binary XOR operation on two input strings consisting of 1s and 0s.

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
        str: Result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Use zip to iterate over characters in the strings in parallel
    # Convert each character to an integer (0 or 1)
    # Calculate the XOR of each pair of characters
    # Convert the result back to a string
    return ''.join('1' if (int(i) + int(j)) % 2 == 1 else '0' for i, j in zip(a, b))

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This script defines the `string_xor` function, which takes two binary strings as input and returns their XOR result as a string. It uses a generator expression to iterate over the characters in the input strings, calculate the XOR of each pair of characters, and convert the result back to a string. The script also includes test cases to demonstrate the function's behavior.