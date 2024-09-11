```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two input strings 
    consisting only of 1s and 0s and returns the result as a string.

    Args:
        a (str): The first input string consisting only of 1s and 0s.
        b (str): The second input string consisting only of 1s and 0s.

    Returns:
        str: The result of binary XOR operation on input strings as a string.

    Raises:
        ValueError: If input strings do not consist only of 1s and 0s.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Check if input strings have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")

    # Perform binary XOR operation on input strings
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    return result


# Test the function
print(string_xor('010', '110'))  # Output: '100'
```