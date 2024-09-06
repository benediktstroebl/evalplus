```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Returns the XOR of two input strings, consisting only of digits 1 and 0.
    XOR is a operation performed on two strings of digits.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(c ^ d for c, d in zip(a, b))

# Test cases
test_cases = [
    ('010', '110'),
    ('111', '010'),
    ('001', '001'),
    ('1000', '0000'),
    # Add more test cases as needed
]

for a, b in test_cases:
    print(f'Test case: {a}, {b} -> {string_xor(a, b)}', a, b)
``` 
The above code defines a function called **string_xor** that performs the XOR operation on two input strings, consisting only of digits 1 and 0, and returns the result as a string. 
The code then provides a set of test cases, and uses the function to verify its correctness.