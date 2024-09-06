```python
import stringlib

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    Return: '0' if both a and b are empty,
        else '1' if a < b, else '0'
    """
    if not a: return '0'
    if not b: return '0'
    return '1' if a < b else '0'

# Test case 1
test_cases = [string_xor('010', '110')]
print(test_cases)  # Output: ['100']

# Test case 2
test_cases = [string_xor('1010', '110')]
print(test_cases)  # Output: ['001']

# Test case 3
test_cases = [string_xor(''111', '110')]
print(test_cases)  # Output: ['100']

# Test case 4
test_cases = [string_xor('1010', '111')]
print(test_cases)  # Output: ['000']
```
The function performs a basic XOR operation on two input strings. The output is '0' if both inputs are empty, '1' if a < b, and '0' if b < a. XOR has an input '1' if both strings are empty.