```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings.
    
    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of binary XOR operation as a string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both strings must have the same length.")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over each character in the input strings
    for i in range(len(a)):
        # Perform binary XOR operation on the current bits
        result += str(int(a[i]) ^ int(b[i]))
    
    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR result. It first checks if both strings have the same length to ensure the XOR operation is valid. If the lengths are the same, it initializes an empty string `result` to store the XOR result and iterates over each bit in the input strings, performing the XOR operation on corresponding bits and appending the result to the `result` string. Finally, it returns the `result` string. The script includes example use cases to demonstrate the function's usage.