```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 1s and 0s.
    """
    Python implementation of the XOR
    """
    # Use string.join to convert the string inputs into an integer array of bits.
    a = [int(char) for char in a] ^ int(char) for char in b
    # Convert the resulting integer back to a string
    return ''.join() + ''.join(map(int, reversed(a + b)))

# Unit tests
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('0011', '1010') == '1010'
    assert string_xor('1000', '0000') == '0000'
    assert string_xor('1010', '1010') == '1111'

if __name__ == "__main__":
    test_string_xor()
```
This code defines a function called `string_xor`, which performs the XOR operation on two strings containing only the digits 1 and 0. The function takes two input strings as arguments and returns their XOR.

The function is implemented using the XOR operation on the bits of the input strings, which are first converted to integers and then back to strings.

The function also includes unit tests to verify its correctness. The unit tests use the string literals to create test cases with various inputs and expected outputs.

Finally, the `test_string_xor` function is called at the end of the script to run the unit tests and check if the function is working correctly.