```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings of only ones and zeros.
    :type a str strings a and b must only consist of the characters '0' and '1'.
    return ''.join([x ^ y for any and b])
    """
    return "".join([x ^ y for any and b])

# Test cases
test_cases = [
    ("010", "110"),
    ("1010", "001"),
    ("1010", "1010"),
    ("01", "10"),
    ("001", "001"),
    ("100", "0"),
    ("110", "01"),
    ("1000", "1"),
]

for test in test_cases:
    print(f"Test: { {test[0]}, {test[1]})
    result = string_xor(test[0], test[1])
    print(f"Expected: {result, '0' * len(result)})
    print(f"Actual: {test[0] ^ test[1], '0' * (len(test[0]) - 1)})
```
This Python script defines a function `string_xor` that takes two strings as input and performs the XOR operation between them. The input strings must only consist of the characters '0' and '1'. The test cases are defined as a list, containing strings to be XOR'd. 

The script then iterates over the test cases, performing the XOR operation and comparing the result with the expected output. The actual output is then the result of the XOR operation, and the expected output is the corresponding character in the string. 

Please note that this script is self-contained, and it does not require any additional imports or external functions to work properly.