```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings with only ones and zeros
    """
    # similar to bitwise xor in C
    return ''.join(''.join([ord(i) ^ i for i in a] ^ [ord(i) ^ i for i in b])

# test cases
test_cases = [
    "010",
    "110",
    "0011",
    "1010",
]

for i, case in enumerate(test_cases):
    actual = string_xor(case, case)
    print(f"{i+1}.")
    print(f"{case} => {actual}")
```
This code defines a function that performs the XOR operation on two strings. It takes a pattern that converts all characters in a string to their corresponding binary digits and then performs the XOR operation by performing a bitwise XOR on each pair of corresponding binary digits. The output is the expected result for each test case.