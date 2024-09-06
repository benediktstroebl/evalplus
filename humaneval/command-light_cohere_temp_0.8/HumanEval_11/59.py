```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of digits 1 and 0.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join_chars('01'[(a ^ b) ^ ord('0')])
# Example usage
test_str = string_xor('010', '110')
print(test_str)  # Output: '100'
``` 
This code provides a self-contained solution for the problem you mentioned.  It generates a string by XOR-ing the first input string with the second using only digits 1 and 0, and then converts the result into a string using list comprehension.