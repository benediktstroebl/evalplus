```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    This function performs binary XOR operation on two binary strings and returns the result.

    Args:
        a (str): First binary string
        b (str): Second binary string

    Returns:
        str: Result of binary XOR operation on a and b

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if input strings consist only of 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings should consist only of 1s and 0s")

    # Initialize an empty result string
    result = ''

    # Iterate over the characters in the input strings
    for i, j in zip(a, b):
        # Perform binary XOR operation and append the result to the result string
        result += str(int(i) ^ int(j))

    # If the lengths of the input strings are different, append zeros to the result string
    if len(a) > len(b):
        result += '0' * (len(a) - len(b))
    elif len(b) > len(a):
        result += '0' * (len(b) - len(a))

    return result
```
You can test this function with the example you provided:

```python
print(string_xor('010', '110'))  # Outputs: '100'
```