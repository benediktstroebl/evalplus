```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of binary XOR operation as a string.

    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    for i in range(max(len(a), len(b))):
        bit_a = a[len(a) - i - 1] if i < len(a) else '0'
        bit_b = b[len(b) - i - 1] if i < len(b) else '0'
        result = ('1' if (bit_a == '1' and bit_b == '0') or (bit_a == '0' and bit_b == '1') else '0') + result
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
print(string_xor('111', '000'))  # Output: '111'
print(string_xor('101', '101'))  # Output: '000'
```

This script defines a function `string_xor` that performs binary XOR operation on two input strings. It iterates over the characters of the input strings from right to left (i.e., from least significant bit to most significant bit), performs the XOR operation for each pair of bits, and builds the result string by prepending the result of each operation to the left. The function handles input strings of different lengths by padding the shorter string with zeros from the left. The test cases demonstrate the function's correctness for various input combinations.