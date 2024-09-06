```python
import stringio
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings using only 1s and 0s.
    """
   
    stringio with digits converted to their respective XOR characters
    """
    return ''.join(chr((ord(c)-96) if c.isdigit() else 1))

# tests
def test_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('001', '1111') == '110'
    assert string_xor('000', '1111') == '11'
    assert string_xor('1010', '1111') == '1110'
    assert string_xor('111', '001') == '110'
    assert string_xor('00111', '11001') == '0000'

# Driver function
def main():
    print("Testing XOR Function...")
    test_xor()

if __name__ == "__main__":
    main()
```
The script defines a function `string_xor` that performs the XOR operation on two input strings, converting the input characters to their corresponding XOR characters. It also has a test_xor function, which contains several tests to validate the correctness of the `string_xor` function. 

Lastly, the `main()` function is used to drive the execution of the code and run the tests.