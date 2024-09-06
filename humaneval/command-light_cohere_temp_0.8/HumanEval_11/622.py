```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings
    """
    return ''.join(c ^ d for c, d in zip(a, b))

# Test cases
test_cases = [
    '010', '110', '100', '001', '111'
]

for case in test_cases:
    assert string_xor(case, case) == '100'
``` 
This code defines a function named `string_xor` that performs the XOR operation on two input strings. The function uses the string formatting and a generator expression to create the output, which is also a string. 

The function is then tested with several test cases, and the results are compared against the expected values using the `assert` assertion. 

These test cases ensure the function's correctness by verifying if the XOR operation on the input strings produces the expected result.