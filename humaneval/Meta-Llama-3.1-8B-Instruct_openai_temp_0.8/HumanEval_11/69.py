### Binary String XOR
#### Problem Description

Perform binary XOR operation on two binary strings.

#### Solution

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The binary XOR result of strings a and b.
    """
    # Check if inputs consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use map to apply XOR operation on each character in the strings
    # '1' XOR '0' = '1', '0' XOR '0' = '0', '1' XOR '1' = '0'
    xor_result = ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))

    return xor_result


# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
    print(string_xor('111', '000'))  # Output: '111'
    print(string_xor('101', '101'))  # Output: '000'
```

This script defines a function `string_xor` that takes two binary strings as input, performs binary XOR operation on them, and returns the result as a string. It includes a check to ensure the input strings consist only of '1's and '0's. The example usage section demonstrates how to use this function with different input values.