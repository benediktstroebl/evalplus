```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    
    Args:
    a (str): The first input string consisting only of 1s and 0s.
    b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
    str: The result of binary XOR operation as a string.
    
    Raises:
    ValueError: If the input strings are not of the same length or contain characters other than 1s and 0s.
    """

    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Check if the input strings contain only 1s and 0s
    if not set(a).issubset('10') or not set(b).issubset('10'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the current characters and append the result to the result string
        result += str(int(char_a) ^ int(char_b))

    # Return the result string
    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```