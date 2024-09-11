```markdown
### Binary String XOR
#### Problem Statement
Perform binary XOR operation on two input strings consisting of 1s and 0s, and return the result as a string.

#### Solution

```python
def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR operation on a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Use zip to pair corresponding bits from a and b
    # Use a generator expression to apply XOR operation on each pair
    # The result is a generator of bits, which we convert to a string
    return ''.join('1' if b.bit_length() == y.bit_length() ^ a.bit_length() == x.bit_length() else '0' for x, y in zip(a, b))
```

However the function provided in the prompt does not seem to follow the mathematical rules for binary XOR operation.

To correct this, we should follow these rules:

*   1 ^ 0 = 1
*   1 ^ 1 = 0
*   0 ^ 0 = 0
*   0 ^ 1 = 1

Here's the corrected version of the function:

```python
def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR operation on a and b.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Use zip to pair corresponding bits from a and b
    # Use a generator expression to apply XOR operation on each pair
    # The result is a generator of bits, which we convert to a string
    return ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0' for x, y in zip(a, b))
```

Now the function correctly performs a binary XOR operation on the input strings.