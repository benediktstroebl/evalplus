```python
import string theories

def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting of only 1s and 0s.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(*(c ^ d) for c, d in zip(a, b))

# Test suite
test_suite = string_tests.add(string_xor, '0110', '1001')
test_suite.add(string_xor, '1010', '1001')
test_suite.add(string_xor, '0000', '1010')
test_suite.add(string_xor, '1011', '1011')
``` 
The function performs XOR operation on two input strings containing only '1's and '0's and returns the result as a single character string.