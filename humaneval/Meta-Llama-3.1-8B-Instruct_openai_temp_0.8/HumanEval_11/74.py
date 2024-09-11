```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings and return the result.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both inputs must be binary strings (contain only 0s and 1s)")

    # Initialize an empty list to store the result
    result = []

    # Iterate over the inputs
    for i, j in zip(a, b):
        # Perform XOR operation on the current bits and append the result
        result.append(str(int(i) ^ int(j)))

    # Join the result list into a string and return it
    return ''.join(result)


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '011'))  # Output: '110'
print(string_xor('111', '000'))  # Output: '111'
```

This script defines a function `string_xor` that takes two binary strings as input, performs a binary XOR operation on them, and returns the result as a string. It includes input validation to ensure that the inputs are valid binary strings. The function uses the built-in `zip` function to iterate over the inputs in parallel and the `int` and `str` functions to perform the XOR operation and convert the result to a string, respectively. The script also includes test cases to demonstrate the function's usage.