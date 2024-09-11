```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings consisting of 1s and 0s.
    
    Args:
        a (str): The first input string.
        b (str): The second input string.
    
    Returns:
        str: The result of the XOR operation as a string.
    
    Examples:
        >>> string_xor('010', '110')
        '100'
    """
    
    # Check if both inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings.")
    
    # Check if both inputs only contain 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Both inputs must only contain 1s and 0s.")
    
    # Use zip to iterate over characters in both strings in parallel
    # Use a list comprehension to perform XOR operation on each pair of characters
    # Convert the result to a string
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))


# Example usage
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '111'))  # Output: '000'
print(string_xor('000', '000'))  # Output: '000'
```