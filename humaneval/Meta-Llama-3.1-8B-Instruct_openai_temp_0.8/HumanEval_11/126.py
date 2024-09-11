### Binary String XOR
```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings and return the result as a string.

    Args:
        a (str): The first input string consisting of 1s and 0s.
        b (str): The second input string consisting of 1s and 0s.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s.")

    # Perform XOR operation on corresponding bits
    result = ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0' for x, y in zip(a, b))

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '010'))  # Output: '111'
print(string_xor('111', '000'))  # Output: '111'
```
This script defines the `string_xor` function, which takes two input strings `a` and `b` and returns their binary XOR result as a string. It includes input validation to ensure that the input strings consist only of 1s and 0s. The function uses a list comprehension with the `zip` function to perform the XOR operation on corresponding bits and then joins the result into a string. The example usage demonstrates the function's behavior with different input strings.