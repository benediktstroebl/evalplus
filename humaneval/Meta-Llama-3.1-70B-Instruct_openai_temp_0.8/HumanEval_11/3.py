```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings a and b.
    The input strings should consist only of 1s and 0s.
    The result of the XOR operation is returned as a string.

    Args:
        a (str): The first input string consisting of 1s and 0s.
        b (str): The second input string consisting of 1s and 0s.

    Returns:
        str: The result of the binary XOR operation on a and b.
    """

    # Check if the input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length.")

    # Use the zip function to iterate over the characters of the input strings in parallel
    # Use a list comprehension to perform the XOR operation on each pair of characters
    # The XOR operation is performed using the!= operator, which returns True if the characters are different and False otherwise
    # The result is converted to an integer using the int function and then to a string using the str function
    xor_result = ''.join(str(int(x!= y)) for x, y in zip(a, b))

    return xor_result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```