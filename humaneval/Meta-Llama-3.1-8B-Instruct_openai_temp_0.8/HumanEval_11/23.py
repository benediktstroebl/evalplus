```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of performing binary XOR on a and b.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    result = ''.join('1' if (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1') else '0' for i in range(len(a)))
    return result
```

You can run this script and test the function with the example you provided:

```python
print(string_xor('010', '110'))  # Outputs: '100'
```