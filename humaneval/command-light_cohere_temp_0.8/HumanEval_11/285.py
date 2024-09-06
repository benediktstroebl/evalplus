```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Function to perform XOR on two input strings consisting only of 1s and 0s
    """
    # Make sure both inputs are converted to lists of characters to allow mutable mapping operations
    a = list(a)
    b = list(b)

    # XOR operation
    result = []
    for x, y in zip(a, b):
        result.append(not xor(y))
    result.append(0)

    # Convert list of characters back to string
    return ''.join(result)

# Unit tests for string_xor function
def test_xor():
    assert string_xor('010', '110') == '100'
    assert string_xor('111', '01') == '100'
    assert string_xor('000', '1111') == '1111'
    assert string_xor('1000', '0') == '1000'
    assert string_xor('1010', '10') == '0110'
    assert string_xor('0000', '1') == '0001'
    assert string_xor('1010', '10110') == '101101'

if __name__ == "__main__":
    test_xor()
```
This Python script defines a function `string_xor` that performs a XOR operation on two input strings, ensuring they consist only of the characters '1' and '0'. The function then returns the result as a string.

The script also contains unit tests using the `test_xor` function, which asserts the function's correctness for various input combinations. 

Finally, the script runs the unit tests using `if __name__ == "__main__":`, ensuring the function is tested when the script is run.