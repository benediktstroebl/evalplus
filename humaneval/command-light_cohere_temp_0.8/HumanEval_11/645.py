```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros
    Args:
        a: String, First string
        b: String, Second string
    Returns:
        String, Result of XOR operation
    """
    # Validate input
    assert isinstance(a, str) and a and b, "Both inputs must be strings"
    assert len(a) == len(b) == 7, "Both inputs must be 7 characters long"

    # XOR operation
    result = '0' * len(a) + a + b

    return result

def test_string_xor():
    """ Function to test the string_xor function
    """
    assert string_xor("010", "110") == "100", "Failed test case 1"
    assert string_xor("111", "11") == "10", "Failed test case 2"
    assert string_xor("000", "0000") == "0000", "Failed test case 3"
    assert string_xor("1010", "1010") == "1011", "Failed test case 4"
    assert string_xor("1111", "1111") == "1111", "Failed test case 5"

if __name__ == "__main__":
    test_string_xor()
```
This script defines a function `string_xor` that performs a binary XOR operation on two input strings, both consisting of only ones and zeros. It also has a tests the script with a function `test_string_xor` that validates the `string_xor` function against multiple test cases.