Here's the Python code with the function `string_xor` that performs the XOR operation of two input strings, which are composed solely of characters '0' and '1':

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of 0s and 1s.
    :param
        string a (str): two strings
    :return string: their XOR
    """
    # Remove all non-alph characters from each string
    a = ''.join(c for c in a if c == '0')
    b = ''.join(c for c in b if c == '0')

    return ''.join(c for c in a ^1)

# Test cases
test_cases = [
    ('010', '110'),
    ('1010', '0110'),
    ('1010', '110'),
    # Add more test cases here...
]

for case in test_cases:
    actual = string_xor(*case)
    assert actual == case[1]
```

This script defines a function `string_xor` that takes two strings as input and returns their XOR. The test cases ensure the expected output for all the valid combinations of characters.