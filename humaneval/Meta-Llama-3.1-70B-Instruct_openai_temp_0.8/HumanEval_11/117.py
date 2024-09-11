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
        str: The binary XOR result as a string.

    Raises:
        ValueError: If either string contains characters other than '1' or '0'.
    """

    # Check if input strings contain only '1's and '0's
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of '1' and '0'.")

    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length.")

    # Use zip to iterate over characters in both strings in parallel
    # Use a generator expression to perform XOR operation on characters
    # Convert result back to string using join
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

In this script, the `string_xor` function takes two binary strings `a` and `b` as input, checks if they contain only '1's and '0's, and if they have the same length. Then it uses the `zip` function to iterate over the characters of both strings in parallel, performs the XOR operation using a generator expression, and converts the result back to a string using the `join` method. The result is then returned.