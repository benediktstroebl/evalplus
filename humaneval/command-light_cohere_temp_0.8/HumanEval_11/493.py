```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones and zeros. XOR(a,b) = a^1b^1 || a^0b^0
    """
    # Splitting into lists of characters
    al = [c for c in a]
    bl = [c for c in b]

    # XOR of lists of characters
    result = [al[i] ^ bl[i] for i in range(len(al))]

    # Joining the lists back into a string
    return ''.join(result)

# Unit tests
test_str_xor = ['010', '110', '100', '001', '101', '001']
test_strings = [('010', '110'), ('100', '1')]

def test_function(func, strings):
    for test_data in test_strings + test_str_xor:
        got = func(test_data[0], test_data[1])
        expected = ''.join(test_data[1] ^ test_data[0])
        assert got == expected, f"For {test_data}, expected {expected} but got {got}"

# Main function
if __name__ == "__main__":
    test_function(string_xor, test_strings + test_str_xor)
``` 
This script defines a function called `string_xor` that takes two strings as input and returns the XOR of the two input strings. It also includes unit tests to verify the correctness of the `string_xor` function. 

The `test_function` function is used to test the `string_xor` function with various input combinations.