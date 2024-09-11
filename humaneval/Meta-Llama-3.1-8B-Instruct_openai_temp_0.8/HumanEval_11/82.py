### Binary String XOR
#### Problem Statement
Perform binary XOR operation on two given binary strings.

#### Solution
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Binary string resulting from XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if inputs consist only of 1s and 0s
    if set(a).issubset('01') and set(b).issubset('01'):
        # Use zip() to iterate over characters of a and b in parallel
        # Use a list comprehension to apply XOR operation
        # Convert the result to a string
        return ''.join('1' if (a_char + b_char) in ['01', '10'] else '0' for a_char, b_char in zip(a, b))
    else:
        # Raise ValueError if inputs are not valid
        raise ValueError("Inputs must consist only of 1s and 0s")
```

#### Example Usage
```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'

# Test invalid input
try:
    print(string_xor('101', 'abc'))
except ValueError as e:
    print(e)  # Output: Inputs must consist only of 1s and 0s
```