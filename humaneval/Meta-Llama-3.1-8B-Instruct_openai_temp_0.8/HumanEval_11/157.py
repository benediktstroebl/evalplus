### Binary String XOR in Python

Here's a Python function that performs binary XOR on two strings consisting of 1s and 0s.

```markdown
### Usage
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of the binary XOR operation as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if strings consist only of 1s and 0s
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")

    # Perform XOR operation
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
```

### Explanation

*   We first check if both input strings `a` and `b` consist only of 1s and 0s using the `issubset` method of the `set` class.
*   Then, we use the `zip` function to pair corresponding bits from the two input strings.
*   We perform the XOR operation on each pair of bits by converting them to integers, applying the XOR operator (`^`), and converting the result back to a string.
*   Finally, we join the resulting bits together into a single string using the `join` method.

### Example Usage

```python
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```