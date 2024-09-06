```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two input strings using ASCII character
    representation.
    Parameters:
    str a, str b
    Returns: str
    """
    # Check if both inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings")

    # Check if lengths of both inputs are equal
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")

    # Check if both inputs contain only digits
    if not all(c in '0123456789' for c in a + b):
        raise ValueError("Input strings must contain only digits")

    return a ^ b
```