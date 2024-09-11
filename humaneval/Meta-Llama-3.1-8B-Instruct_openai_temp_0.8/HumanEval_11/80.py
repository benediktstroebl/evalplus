### Binary XOR of Two Binary Strings
#### Problem Description
We are given two binary strings `a` and `b` consisting only of 1s and 0s. We need to perform a binary XOR operation between the two strings and return the result as a string.

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
        str: The binary XOR result of a and b as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    return result

# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

#### Explanation
The `string_xor` function takes two binary strings `a` and `b` as input and returns their binary XOR result as a string. It first checks if both strings have the same length to ensure that the XOR operation is valid. Then, it iterates over the characters in the strings using the `zip` function, performs the XOR operation on each pair of characters, and appends the result to a new string. Finally, it returns the resulting string.