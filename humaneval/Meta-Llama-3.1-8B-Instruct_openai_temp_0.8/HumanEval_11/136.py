### Binary String XOR Operation
#### Problem Statement

Perform binary XOR operation on two input strings, each consisting of 1s and 0s, and return the result as a string.

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
        str: The binary XOR of a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Initialize an empty list to store the result
    result = []

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters and append the result
        result.append(str(int(char_a) ^ int(char_b)))

    # Join the result list into a string and return it
    return ''.join(result)


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '110'))  # Output: '011'
```

In this solution, we use the `zip` function to iterate over the characters of the input strings in parallel. We perform the XOR operation on each pair of characters using the `^` operator and convert the result to a string using the `str` function. The `int` function is used to convert the character to an integer (either 0 or 1) before performing the XOR operation. Finally, we join the result list into a string using the `join` method.