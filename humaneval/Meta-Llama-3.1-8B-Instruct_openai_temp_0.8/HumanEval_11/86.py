### Binary String XOR
#### Problem Statement
Perform binary XOR operation on two binary strings and return the result as a string.

#### Solution
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings and return the result as a string.

    Args:
    a (str): First binary string.
    b (str): Second binary string.

    Returns:
    str: Result of binary XOR operation as a string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Iterate over the characters in both strings
    for char_a, char_b in zip(a, b):
        # Perform binary XOR operation and append the result to the string
        result += str(int(char_a) ^ int(char_b))

    return result
```
#### Example Usage
```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```
Note: This solution assumes that both input strings have the same length. If the strings have different lengths, the function will only process the characters up to the length of the shorter string.