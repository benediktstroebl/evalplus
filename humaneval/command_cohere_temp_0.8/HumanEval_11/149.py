```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:]
```

This Python script solves the problem by taking two input strings, `a` and `b`, which are supposed to consist only of 1s and 0s. It performs binary XOR on these inputs, converts the result back to a string format, and returns it. This is achieved by using the `int` function to convert both input strings to integer values in binary representation, performing the XOR operation using the bitwise XOR operator `^`, and then converting the result back to a string using the `bin` function.

Here's an example of how you can use this function to test its functionality:
```python
# Test the string_xor function
assert string_xor('010', '110') == '100'
```

This will verify that the function behaves as expected, resulting in the correct output of '100' when performing binary XOR on the inputs '010' and '110'.