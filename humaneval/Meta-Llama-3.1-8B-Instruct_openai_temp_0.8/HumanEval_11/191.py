### Binary String XOR Function
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs a binary XOR operation on two input strings.

    The input strings are expected to consist only of 1s and 0s.
    The result is also returned as a string.

    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation on the input strings.
    """
    # Check if both strings have the same length
    if len(a)!= len(b):
        raise ValueError("Both input strings must have the same length.")

    # Use the zip function to iterate over the characters of both strings in parallel
    # Use a list comprehension to create a list of XOR results
    # The XOR operation is performed using the ^ operator
    result = [str(int(a_i) ^ int(b_i)) for a_i, b_i in zip(a, b)]

    # Join the list of XOR results into a single string
    return ''.join(result)

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. The function first checks if the input strings have the same length to ensure that the XOR operation is valid. It then uses a list comprehension to iterate over the characters of both strings in parallel, performs the XOR operation on each pair of characters using the `^` operator, and joins the results into a single string using the `join` method. The example usage demonstrates how to use the `string_xor` function to perform a binary XOR operation on two binary strings.