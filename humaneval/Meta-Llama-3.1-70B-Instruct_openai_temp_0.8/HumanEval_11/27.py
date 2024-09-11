```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Parameters:
    a (str): The first binary string consisting only of 1s and 0s.
    b (str): The second binary string consisting only of 1s and 0s.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    
    # Check if inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings.")

    # Check if inputs consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both inputs must consist only of 1s and 0s.")

    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Both inputs must have the same length.")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the input strings
    for i in range(len(a)):
        # Perform XOR operation on the current characters
        # In Python, the XOR operator is ^
        # The int function is used to convert the characters to integers
        # The str function is used to convert the result back to a string
        result += str(int(a[i]) ^ int(b[i]))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR as a string. It checks if the inputs are valid (i.e., strings consisting only of 1s and 0s and having the same length), and then performs the XOR operation on the characters of the input strings. The result is returned as a string. The script also includes a test case to demonstrate the function's usage.