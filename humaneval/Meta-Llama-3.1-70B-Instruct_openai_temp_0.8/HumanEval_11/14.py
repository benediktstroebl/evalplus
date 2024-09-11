```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings a and b, 
    which consist only of 1s and 0s, and return the result as a string.

    Args:
        a (str): The first string of 1s and 0s.
        b (str): The second string of 1s and 0s.

    Returns:
        str: The result of the binary XOR operation as a string.

    Raises:
        ValueError: If either a or b contains characters other than '0' and '1'.
    """

    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length.")

    # Check if both strings consist only of '0' and '1'
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both strings must consist only of '0' and '1'.")

    # Initialize an empty result string
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR on the current characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    return result


# Example usage:
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
```