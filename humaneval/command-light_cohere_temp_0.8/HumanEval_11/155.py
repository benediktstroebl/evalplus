```python
import stringio
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on the inputs and return result also as a string.
    """
    def __init__(self, a: str, b: str) -> None:
        self.a = a stringio in(a, b)
    if len(a) != len(b):
        raise ValueError("Input strings must be the same length.")

    # split the inputs to be able to xor them in binary
    a_binary = []
    b_binary = []
    for char in a:
        a_binary.append(2 if char == '0' else 1)
    for char in b:
        b_binary.append(2 if char == '0' else 1)

    # XOR the binary numbers
    xored_bits = []
    for i in range(len(a_binary)):
        xored_bits.append(a_binary[i] ^ b_binary[i])

    # Concatenate the xored bits to form the result string
    result = ''
    for bit in xored_bits:
        result += bit

    return result


def test():
    """
    Test the function
    a = '010'
    b = '110'
    result = string_xor(a, b)
    print(result)
    assert result == '100'
``` 
The code defines a function `string_xor` that performs a binary XOR operation on two input strings, and returns the result as a string. The test function verifies that expected output of the function for a given pair of input strings.