```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a) // 3)
```

The provided Python script defines a function called `string_xor` that takes two strings `a` and `b` as input. This function performs a binary XOR operation on the bits of `a` and `b`. This operation is carried out by converting the input strings to their corresponding binary integers using the `int` function followed by bitwise XOR using the `^` operator. The resulting binary value is then converted back to a string format using `bin`, and the leading '0b' is removed using `[2:].zfill(len(a) // 3)`. The output of this function is the binary string that results from the XOR operation between the input strings.

Here is an example usage of the function and its test:
```python
def test_string_xor():
    # Test case
    assert string_xor('010', '110') == '100'

test_string_xor()
```
The test case checks if the output of the function `string_xor` is correct for the input strings `'010'` and `'110'`. The assert statement compares the result with the expected output, `'100'`, ensuring that the function produces the desired output for this specific case.

The test is executed successfully as the assert statement does not throw an error, confirming the accuracy of the function's implementation for this particular test case.