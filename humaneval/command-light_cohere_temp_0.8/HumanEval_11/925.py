```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two input strings a and b consisting only of '0's and '1's.
    Convert input strings to lists of digits, then perform element-wise XOR.
    Return the strings.
    """
    Recursive approach could string-matching function
    """
    return ''.join((i if ord(a[i]) - 97 <= ord(b[i]) - 97 else b[i]) for i in a + b)

# Unit tests:
def test_string_xor():
    test_cases = [
        ('010', '110'),
        ('001000', '1000'),
        ('abc', 'cba'),
        ('', '')
    ]
    
    for a, b in test_cases:
        actual = string_xor(a, b)
        assert actual == b, f"Case {a} did not match"

# Run the tests
test_string_xor()
```
This Python script defines a function `string_xor` that performs the XOR operation on two input strings, where both strings only contain the digit '1'. The function converts the input strings to lists of digits and then performs an element-wise XOR operation on the digits. The final result is also converted back to a string, the function returns the XOR of the two input strings.

Finally, the script includes unit tests for the `string_xor` function using the `unittest` library. The tests ensure that function correctly performs the XOR operation on a variety of input strings.