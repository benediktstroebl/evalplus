```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Returns the XOR of two input strings consisting only of 1s and 0s."""
    return ''.join([i ^ j for i in '01' for i, j in zip(a, b)])

# Test the function with different inputs
# Test with all single characters
test_cases = ['1', '0', 'a', 'A']
test_results = [string_xor(test_cases[0], test_cases[1])]
print(test_results)  # Output should be 10


# Test with different strings
test_cases = ['Test String', 'Testing', 'Code']
test_results = [string_xor(test_cases[1], test_cases[2])]
print(test_results)  # Output should be 000


# Test with different characters
test_cases = ['10', 'a', 'A']
test_results = [string_xor(test_cases[0], test_cases[1])
print(test_results)  # Output should be 1


# Test with different lengths
test_cases = ['', 'a', ' ', '10', '11']
test_results = [string_xor(test_cases[1], test_cases[3])
print(test_results)  # Output should be 101
```