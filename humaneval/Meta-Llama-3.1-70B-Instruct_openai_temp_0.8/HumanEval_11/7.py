```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first input string.
    b (str): The second input string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If either input string contains characters other than 1 and 0.
    """

    # Check if input strings contain only 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Initialize an empty list to store the result
    result = []

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the current characters
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the list
        result.append(xor_result)

    # Join the result list into a string and return
    return ''.join(result)


# Example usage
print(string_xor('010', '110'))  # Output: '100'
```
This script defines a function `string_xor` that takes two input strings `a` and `b`, performs a binary XOR operation on the corresponding characters of the strings, and returns the result as a string. The function includes error checking to ensure that the input strings contain only 1s and 0s and have the same length. The example usage at the end demonstrates how to use the function with the provided test case.