### Binary String XOR Function
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Use the built-in zip function to iterate over the characters in the input strings in parallel
    # The XOR operation is performed using the ^ operator, which works on individual bits
    # The result is converted back to a string using the join function
    return ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0'
                   for x, y in zip(a, b))
```
### Example Usage
```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '011'))  # Output: '110'
```