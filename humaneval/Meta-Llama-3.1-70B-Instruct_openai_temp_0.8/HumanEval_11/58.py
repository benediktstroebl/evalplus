```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two input strings consisting of 1s and 0s.

    Args:
        a (str): First input string consisting of 1s and 0s.
        b (str): Second input string consisting of 1s and 0s.

    Returns:
        str: Result of binary XOR operation on input strings as a string.

    Raises:
        ValueError: If input strings are not of the same length or contain characters other than 1s and 0s.

    Example:
        >>> string_xor('010', '110')
        '100'
    """

    # Check if input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")

    # Check if input strings contain characters other than 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")

    # Perform binary XOR operation using zip function and list comprehension
    result = ''.join('1' if bit_a!= bit_b else '0' for bit_a, bit_b in zip(a, b))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: 100
```

In this script, the `string_xor` function takes two input strings `a` and `b` and performs a binary XOR operation on them. The result is returned as a string. The function includes input validation to ensure that the input strings are of the same length and consist only of 1s and 0s. If the input is invalid, a `ValueError` is raised with an appropriate error message.