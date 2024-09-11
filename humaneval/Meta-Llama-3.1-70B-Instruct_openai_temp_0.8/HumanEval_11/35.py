```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
    a (str): The first input string consisting only of 1s and 0s.
    b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    
    Raises:
    ValueError: If either of the input strings contains characters other than 1s and 0s.
    """

    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length")

    # Check if the input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the characters
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the output string
        result += xor_result

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'

# Test the function with invalid inputs
try:
    print(string_xor('012', '110'))  # Output: ValueError
except ValueError as e:
    print(e)  # Output: Input strings must consist only of 1s and 0s

try:
    print(string_xor('010', '1100'))  # Output: ValueError
except ValueError as e:
    print(e)  # Output: Input strings must be of the same length
```