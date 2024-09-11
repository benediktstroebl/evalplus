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
    str: The binary XOR result of a and b.

    Raises:
    ValueError: If a or b contains characters other than '0' or '1'.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are valid
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings should only contain '0' and '1'.")

    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings should be of the same length.")

    # Initialize result string
    result = ""

    # Perform XOR operation on each character of the input strings
    for char_a, char_b in zip(a, b):
        # XOR operation
        result += str(int(char_a) ^ int(char_b))

    return result


# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```