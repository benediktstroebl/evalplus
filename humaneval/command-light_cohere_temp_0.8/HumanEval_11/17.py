```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros
    """
    return "".join(c ^ int(a[i]) for i, c in enumerate(b))

# test cases
test_cases = [
    ("010", "110"),
    ("000", "111"),
    ("00110", "10110"),
    ("00", "11"),
    ("100000000", "1110000000")
]

for case in test_cases:
    print(f"Result: {case[0]} XOR {case[1]} = {string_xor(case[0], case[1])}")
```
This script defines a function `string_xor` that performs the XOR operation on two strings, where both strings contain only the digit '1' and the digit '0'. The function then returns the result of the XOR operation. 
For the test cases provided, the script prints the result of each test, showing the expected output.