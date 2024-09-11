```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
        a (str): The first string consisting only of 1s and 0s.
        b (str): The second string consisting only of 1s and 0s.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    
    Raises:
        ValueError: If the input strings are not of the same length or contain characters other than 1 and 0.
    """

    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Check if the input strings contain characters other than 1 and 0
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Initialize an empty result string
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR on the current characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```