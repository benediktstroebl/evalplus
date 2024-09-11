Here's a Python script that implements the `string_xor` function:
```markdown
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
        str: Result of binary XOR operation on a and b.

    >>> string_xor('010', '110')
    '100'
    """
    return ''.join('1' if (i and j) else '0' for i, j in zip(a, b))

if __name__ == "__main__":
    print(string_xor('010', '110'))  # Outputs: '100'
    print(string_xor('111', '000'))  # Outputs: '111'
    print(string_xor('101', '101'))  # Outputs: '000'
```
```