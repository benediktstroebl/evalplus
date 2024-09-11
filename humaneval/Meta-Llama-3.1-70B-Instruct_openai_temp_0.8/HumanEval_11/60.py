```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
    a (str): The first input string.
    b (str): The second input string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Raises:
    ValueError: If either input string contains characters other than '0' or '1'.
    """

    # Check if input strings are valid
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must only contain '0' and '1'")

    # Check if input strings are of equal length
    if len(a)!= len(b):
        raise ValueError("Input strings must be of equal length")

    # Perform XOR operation
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    
    return result


# Test the function
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Expected output: '100'
    print(string_xor('101', '001'))  # Expected output: '100'
    print(string_xor('111', '111'))  # Expected output: '000'
```