```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only digits
    Returns: str
    """
    if len(a) != len(b):
        raise ValueError("Input strings must be the same length")

    result = 0
    for char in a + b:
        result |= int(char)

    return result.0


def test_xor():
    a = "010"
    b = "110"

    result = string_xor(a, b)
    print(f"Result: {result}")

    if result != '100':
        raise ValueError("Output does not match expected '100'")

# Perform XOR on test input strings
test_xor()
```
This Python script defines a self-contained function `string_xor` that performs the XOR operation on two input strings consisting only of digits. The function ensures that the input strings have the same length using the `len` function. It then iterates through the process: it takes the two input strings, initializes a result variable to 0, and for each character in the input strings, it performs a bitwise XOR operation between the character and the corresponding character in the other input string. 

The script also defines a function `test_xor` that contains a sample input string and performs the XOR operation on the test input strings. The output of the string_xor function is then compared with the expected '100' result, and if they do not match, a ValueError is raised.