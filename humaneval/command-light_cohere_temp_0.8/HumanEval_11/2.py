Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones.
    a = a + b
    return a + b

def test():
    xor_str = string_xor('010', '110')
    assert xor_str == '100'

test_list = [test]()
``` 
This script defines a function called `string_xor` that performs the XOR operation of two input strings. It also defines a single function `test` which contains a `assert` statement that verifies if the `string_xor` function returns the correct result for the given inputs.