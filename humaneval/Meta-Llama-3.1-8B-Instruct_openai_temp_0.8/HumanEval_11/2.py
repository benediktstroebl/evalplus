```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Args:
        a (str): A string of 1s and 0s.
        b (str): A string of 1s and 0s.
    
    Returns:
        str: The result of binary XOR operation as a string.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """
    
    # Check if both inputs are valid
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Inputs must consist only of 1s and 0s")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the inputs, performing XOR operation
    for char_a, char_b in zip(a, b):
        # Convert characters to integers, perform XOR operation, and convert back to string
        result += str(int(char_a) ^ int(char_b))
    
    # If one of the inputs is longer than the other, append the remaining characters
    if len(a) > len(b):
        result += a[len(b):]
    elif len(b) > len(a):
        result += b[len(a):]
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '011'))  # Output: '110'
```

This Python script defines a function `string_xor` that performs binary XOR operation on two input strings. The function checks if the inputs are valid, initializes an empty string to store the result, and then iterates over the characters in the inputs, performing XOR operation and appending the result to the string. If one of the inputs is longer than the other, the function appends the remaining characters. The script also includes test cases to demonstrate the function's correctness.