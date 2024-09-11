### Binary String XOR
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Use zip to iterate over characters in both strings, and the operator.itemgetter(0) to get the first element of the tuple
    # The XOR operation is performed using the '!=' operator which returns True for different characters and False for the same
    # The result is then converted to a string
    result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return result
```

This script uses the built-in Python `zip` function to iterate over two input strings at the same time, and a generator expression to perform the binary XOR operation. The `join` function is used to convert the result back into a string. This script assumes that the input strings consist only of 1s and 0s.