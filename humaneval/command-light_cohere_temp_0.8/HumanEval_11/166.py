Here's the improved code with detailed comments and correct type annotations:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Function to perform XOR of two input strings consisting of only digits """

    # Make sure both inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings")

    # Check if both inputs are empty
    if not a or not b:
        raise ValueError("Both inputs cannot be empty")

    # Convert strings to lists of digits for XOR operation
    a = [c for c in a if c in '0']
    b = [c for c in b if c in '0']

    # XOR the digits of both strings
    result = [x ^ y for x, y in zip(a, b)]

    # Join the results back into a string
    return ''.join(result)
```
The function `string_xor` takes two input strings `a` and `b` and returns the result of the XOR operation between the two strings. The function performs type type annotations and ensures that the inputs are valid strings.