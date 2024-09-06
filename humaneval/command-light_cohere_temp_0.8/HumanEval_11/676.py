```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    Returns the XOR of a and b
    """
    # check if the length of the input strings is equal
    if len(a) != len(b):
        raise ValueError("Input strings must be the same length")

    # convert the input strings to list of digits to perform bitwise xor
    a = [int(c) for c in a]
    b = [int(c) for c in b]

    # perform the bitwise XOR operation
    xor_result = [x ^ y for x, y in zip(a, b)]

    # convert the result back to a string
    xor_result_str = ''.join('0' if x == 0 else str(x))
    return xor_result_str

# Example usage
a = '010'
b = '110'
result = string_xor(a, b)
print(result)  # Output: 100
``` 
This code defines a function string_xor that performs the XOR operation on two input strings a and b. The function first checks if the strings have the same length, and raises a ValueError if not. It then converts the string to lists of integers and performs the bitwise XOR operation using a list comprehension. Finally, it converts the result back to a string and returns the XOR of the input strings.