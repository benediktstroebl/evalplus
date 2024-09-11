```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function takes two binary strings as input, performs binary XOR operation and returns the result as a string.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.
    """
    # Check if the input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use the map function to perform XOR operation on corresponding characters
    # The XOR operation is performed by using the ^ operator, which returns 1 if the bits are different and 0 if the bits are the same
    result = ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))

    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('1010', '1100'))  # Output: '0110'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation, and returns the result as a string. It also includes test cases to demonstrate the function's behavior. The function first checks if the input strings consist only of 1s and 0s, and raises a `ValueError` if they do not. The XOR operation is performed using the `map` function and a lambda function, which applies the XOR operation to corresponding characters in the input strings. The result is then joined into a string using the `join` method.