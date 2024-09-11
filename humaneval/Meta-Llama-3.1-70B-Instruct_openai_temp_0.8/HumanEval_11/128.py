```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings and return the result as a string.

    Args:
        a (str): The first input string consisting only of 1s and 0s.
        b (str): The second input string consisting only of 1s and 0s.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either input string contains characters other than 1 and 0.

    Examples:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs are valid
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Initialize result string
    result = ''

    # Iterate over characters in input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR on corresponding characters
        xor_result = str(int(char_a) ^ int(char_b))
        # Append result to output string
        result += xor_result

    return result

# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```