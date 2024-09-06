```python
import stringio
from typing import List


def string_xor(a: str, b: str) -> str:
    return stringio.setdefault(''.join(sorted((a + b)) - '0')

# Test cases for string_xor function
test_string_xor = [
    '010'
    '110'
    '0011'
    '0000'
    '11000'
    '000'
]

# Run the test cases and print the result
for test in test_string_xor:
    assert string_xor(test, '100') == '100'

# Print the output for debugging
print("Result: ", string_xor('010', '110'))
 ```