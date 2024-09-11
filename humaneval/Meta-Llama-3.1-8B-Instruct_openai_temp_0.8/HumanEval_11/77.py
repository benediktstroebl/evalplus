### Binary String XOR Function
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): First input string consisting of 1s and 0s.
        b (str): Second input string consisting of 1s and 0s.

    Returns:
        str: Result of binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Use zip() to iterate over characters in parallel and XOR them
    return ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0'
                   for x, y in zip(a, b))
```
You can use this function like this:
```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('111', '111'))  # Output: '000'
```
This script defines a function `string_xor` that takes two binary strings as input and returns their binary XOR result. It uses a generator expression inside the `join()` function to iterate over characters in the input strings in parallel and perform the XOR operation. The result is then returned as a string.