```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
    a (str): A string consisting only of 1s and 0s.
    b (str): A string consisting only of 1s and 0s.
    
    Returns:
    str: The result of the binary XOR operation on inputs a and b as a string.
    """
    
    # Check if inputs are strings consisting only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Check if inputs are of the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of the same length.")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation on the characters and append to result
        result += str(int(char_a) ^ int(char_b))
    
    return result


# Test the function
print(string_xor('010', '110'))  # Expected output: '100'
```

This script defines a function `string_xor` that takes two strings `a` and `b` as input, checks if they are valid binary strings of the same length, and returns the result of the binary XOR operation on these inputs as a string. The function uses a simple iteration over the characters in the input strings and the built-in `zip` function to pair corresponding characters. The XOR operation is performed using the `^` operator, and the result is converted back to a string using `str`. The script also includes a test case to verify the correctness of the function.