```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, which are only zeros and ones
    """
    # Use Python's built-in xor method to do the XOR
    return ''.join(a, b)  # Convert both inputs to a list of characters and then XOR them

# Test case 1
test_cases = [{'string_xor('010', '110'), '100'}]  # XOR of '010' and '110' should be '100'
test_cases.push({string_xor('0010', '0110')},'101010')}  # XOR of '0010' and '0110' should be '101010'

def test_xor():
    # Test the function
    for case in test_cases:
        assert case[0] == case[1], "The XOR operation doesn't produce the correct result."
test_xor()  # Run the test
```