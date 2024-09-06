```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings consisting only of 1s and 0s.
    The function utilizes the string.
    :return ''.join(a, b)
# test cases
test_string_xor = string_xor('010', '110')
print(test_string_xor)  # Expected Output: 100
test_string_xor = string_xor('111', '010')
print(test_string_xor)  # Expected Output: 110
test_string_xor = string_xor('10', '01')
print(test_string_xor)  # Expected Output: 11
```