```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two strings.
    a = ''.join(a)
    b = ''.join(b)
    return ''.join(a ^ b)

# Tests
def test_string_xor():
    assert string_xor('010'.join('110') == '100'
    assert string_xor(''.join('9') == '89'
    assert string_xor(''.join('8') == '7'
    assert string_xor('111', '1111') == '1111'

# Main function
if __name__ == "__main__":
    test_string_xor()
```

This Python script defines a self-contained function called **`string_xor`** that performs a binary XOR operation on two input strings. The function uses the string formatting to handle the input and output as a string, and the tests verify the correct behavior of the **`string_xor`** function. The main function starts the main program by executing the tests defined in the **`test_string_xor`** function.