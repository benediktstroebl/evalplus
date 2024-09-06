```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of digits '0' and '1'.
    """
    # Convert to lists of digits
    a = list(filter(str.isdigit, a))
    b = list(filter(str.isdigit, b))
    # XOR
    return ''.join(a ^ b)

# Unit tests
def test_string_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '010') == '001'
    assert string_xor('001', '001') == '0000'
    assert string_xor('000', '1111') == '1111'

if __name__ == "__main__":
    test_string_xor()
```
This code defines a function named `string_xor` that performs the XOR operation on two input strings consisting only of the digits '0' and '1'. It uses list comprehension to convert the input strings into lists of digits, and then performs the XOR operation using the ^ operator. The output is a same string. 
Then, the code includes unit tests for the `string_xor` function using the `assert` function. The tests check the string inputs with the expected output.