```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings consisting only of 1s and 0s.
    
    Args:
        a (str): The first binary string.
        b (str): The second binary string.
    
    Returns:
        str: The result of XOR operation as a binary string.
    
    Raises:
        ValueError: If either of the input strings contains characters other than 1s and 0s.
    """
    
    # Check if input strings contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation and convert the result to string
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the list
        result.append(xor_result)
    
    # Join the list into a string and return the result
    return ''.join(result)


# Test the function
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Expected output: '100'
```