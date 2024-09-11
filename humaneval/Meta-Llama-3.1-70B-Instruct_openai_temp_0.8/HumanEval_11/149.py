```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    
    Args:
        a (str): The first input string consisting only of 1s and 0s.
        b (str): The second input string consisting only of 1s and 0s.
    
    Returns:
        str: The result of the binary XOR operation as a string.
    
    Raises:
        ValueError: If either of the input strings contains characters other than 1s and 0s.
    """
    
    # Check if the input strings contain only 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the current characters
        # The XOR operation in Python can be performed using the '^' operator
        # However, since we are dealing with strings, we use the int() function to convert the characters to integers
        # We use the str() function to convert the result back to a string
        result += str(int(char_a) ^ int(char_b))
    
    # Return the result
    return result


# Example usage
print(string_xor('010', '110'))  # Output: '100'
```