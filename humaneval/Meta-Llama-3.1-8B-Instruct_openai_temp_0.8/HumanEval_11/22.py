### Binary XOR of Two Binary Strings
#### Problem Statement
Given two binary strings `a` and `b`, consisting only of 1s and 0s, we need to perform a binary XOR operation on them and return the result as a string.

#### Solution
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary input strings and return the result.

    Args:
    a (str): First binary input string.
    b (str): Second binary input string.

    Returns:
    str: Binary XOR result of a and b.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty string to store the result
    result = ''

    # Ensure both strings have the same length
    max_len = max(len(a), len(b))

    # Perform XOR operation on corresponding bits
    for i in range(max_len):
        # Get the current bits from both strings (or 0 if out of range)
        bit_a = a[-(i + 1)] if i + 1 <= len(a) else '0'
        bit_b = b[-(i + 1)] if i + 1 <= len(b) else '0'

        # Perform XOR operation on the current bits
        result_bit = '1' if bit_a!= bit_b else '0'

        # Prepend the result bit to the result string
        result = result_bit + result

    return result
```

#### Example Usage
```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```