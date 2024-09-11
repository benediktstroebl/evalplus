```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings 
    consisting only of 1s and 0s and returns the result as a string.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of binary XOR operation on the input strings.

    Raises:
        ValueError: If the input strings contain characters other than 1s and 0s.
    """
    
    # Check if the input strings contain characters other than 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings should only contain 1s and 0s")

    # Check if the input strings are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings should be of the same length")

    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the characters
        # The XOR operation returns 1 if the characters are different, 0 if they are the same
        xor_result = str(int(char_a) ^ int(char_b))
        
        # Append the result to the result string
        result += xor_result

    # Return the result string
    return result


# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```