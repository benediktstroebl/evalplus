```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Function performs a bitwise XOR operation on two input strings a and b,
    and returns the result as a string.
    """
    string_xor('010', '110')
    # Output: 100
    """
    return f"{a XOR b}"

# Test string_xor function
def test_xor():
    assert string_xor("010", "110") == "100"

# Test string_xor function with invalid inputs
def test_invalid():
    assert string_xor("abc", "1010") ==" XOR not valid input"

# Run all tests
test_xor()
test_invalid()

```
The code defines a function `string_xor` that performs a bitwise XOR operation on two input strings and returns the result. It also includes a test cases for `string_xor` that cover both valid and invalid inputs. The code uses the using Python's `typing` module to add type hints for better code readability and maintainability.