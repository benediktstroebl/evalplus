```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings and return the result as a string.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The binary XOR result of a and b as a string.
    
    Raises:
        ValueError: If either a or b contains characters other than '0' or '1'.
    """
    
    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain '0' or '1'.")

    # Check if strings are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length.")

    # Initialize an empty result string
    result = ""

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR on the current characters
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the XOR result to the result string
        result += xor_result

    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```