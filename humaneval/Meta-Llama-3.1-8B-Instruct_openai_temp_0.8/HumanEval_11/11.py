```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings and return the result as a string.

    Args:
    a (str): The first binary string consisting only of 1s and 0s.
    b (str): The second binary string consisting only of 1s and 0s.

    Returns:
    str: The binary XOR of the input strings as a string.

    Examples:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if both inputs are strings
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings.")

    # Check if both strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Both inputs must consist only of 1s and 0s.")

    # Use zip() to pair corresponding characters from both strings
    # Use a list comprehension to perform binary XOR on each pair of characters
    # Convert the result to a string
    return ''.join('1' if a_char == '1' and b_char == '0' or a_char == '0' and b_char == '1' else '0' 
                    for a_char, b_char in zip(a, b))
```

This script performs binary XOR on two input strings `a` and `b` and returns the result as a string. It includes type checking and input validation to ensure that both inputs are strings consisting only of 1s and 0s.