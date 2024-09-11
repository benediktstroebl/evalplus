```python
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    This function takes two binary strings as input, performs a binary XOR operation on them, 
    and returns the result as a binary string.

    Args:
        a (str): A binary string consisting of 1s and 0s.
        b (str): A binary string consisting of 1s and 0s.

    Returns:
        str: A binary string resulting from the XOR operation on input strings a and b.
    """
    return ''.join('1' if (x == '1' and y == '0') or (x == '0' and y == '1') else '0' 
                   for x, y in zip(a, b))


# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('101', '101'))  # Output: '000'
print(string_xor('111', '000'))  # Output: '111'
```

This code uses a generator expression within the `join` method to perform the binary XOR operation on each pair of corresponding bits in the input strings `a` and `b`. The `zip` function is used to iterate over the characters of `a` and `b` in parallel. The result is a new binary string where each bit is the XOR of the corresponding bits in the input strings.