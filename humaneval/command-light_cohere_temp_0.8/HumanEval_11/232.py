```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Function performs binary XOR operation on two strings consisting of only '0's and '1's.
    Returns the string of length same length of the input strings, with '0's XORed together.
    """ XOR operation, when the two inputs are '1010' and '1001', the output is '1010'.
    """
    # Convert input strings to lists of binary digits
    ab = [int(ch) for ch in a]
    bb = [int(ch) for ch in b]

    # XOR the binary digits
    result = '0'
    for i in range(len(ab)):
        result += ab[i] ^ bb[i]
    return result

# Test cases
test_cases = [
    ("010", "110"),
    ("1010", "1011"),
    ("1111", "1111"),
    # Add more test cases here
]

for a, b in test_cases:
    expected = "1010"
    got = string_xor(a, b)
    assert expected == got
```  This code defines a function `string_xor` that performs a binary XOR operation on two input strings consisting only of 0s and 1s. The function converts the string inputs into lists of binary digits, performs the XOR operation, and returns a new string consisting of the XORed digits. The test cases demonstrate the after the function by providing pairs of test strings, and it checks if the result of calling the function with these inputs matches the expected output. 

You can use this code as a reference to build and test your code for this problem.