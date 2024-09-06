```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings.
    Implement both strings only consist of characters '0' and '1'.
    # Convert string to list of characters
    a = ''.join(a)
    b = ''.join(b)
    return ''.join([a[i] ^ b[i] for i in range(0, len(a))])

# Test
test_string = '01010101'
test_result = string_xor(test_string, test_string)
print(test_result)  # Output should be 100
```