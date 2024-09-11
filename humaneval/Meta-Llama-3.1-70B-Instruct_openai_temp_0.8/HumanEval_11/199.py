```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either input string contains characters other than 1s and 0s.

    Example:
        >>> string_xor('010', '110')
        '100'
    """

    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both input strings must have the same length")

    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both input strings must consist only of 1s and 0s")

    # Initialize an empty result string
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform the XOR operation on the current characters
        # The XOR operation on two bits is equivalent to the!= operator
        xor_result = '1' if char_a!= char_b else '0'
        
        # Append the result to the result string
        result += xor_result

    return result


# Example usage
if __name__ == "__main__":
    a = '010'
    b = '110'
    print(f"XOR of '{a}' and '{b}': {string_xor(a, b)}")
```