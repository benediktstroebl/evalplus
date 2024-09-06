```python
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR. The result of the operation is a string consisting of ones and zeros. You can use this function to perform binary XOR on two strings and obtain the result. 

This function utilizes zip to iterate over the characters of both strings `a` and `b` simultaneously, where it calculates the XOR of the corresponding characters' binary values (converted to integers) and converts the result back to a character before joining them into a string. 

The function is self-contained, meaning it does not rely on external variables or functions, and it can be invoked multiple times with different input values to perform binary XOR operations on strings. 

To ensure correct functionality, consider including tests to cover different scenarios like empty input, different string lengths, and various binary patterns. Example test cases are provided below:
```python
def test_string_xor():
    # Test case from the docstring
    assert string_xor('010', '110') == '100'

    # Empty input
    assert string_xor('', '') == ''

    # Different lengths
    assert string_xor('110', '01') == '101'

    # All-ones input
    assert string_xor('1111', '1111') == '0000'

    # All-zeros input
    assert string_xor('0000', '0000') == '1111'

    # Mixed values
    assert string_xor('1100', '1010') == '0110'

test_string_xor()
```

Such tests will cover multiple scenarios and ensure that the `string_xor` function behaves as expected even with edge cases. 
If the python script provided is inserted into a markdown code block, for example, in a competitive programming platform like LeetCode, the test cases can be inserted in an adjacent code block to verify the functionality of the script. 
This approach promotes readability and maintains a self-contained solution, making it readily understandable and usable by others or in collaboration with other platforms or systems.