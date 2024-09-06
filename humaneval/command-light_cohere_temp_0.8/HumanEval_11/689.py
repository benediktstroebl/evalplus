```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings containing only digits.
    Returns the From string concatenation of a and b
    """
    return a + b

# Test case 1
test_cases = [ '010', '110', '100' ]
test_results = [ '100' ]

# Test case 2
test_cases = [ '001000', '111111' ]
test_results = [ '000011' ]

# Test case 3
test_cases = [ 'abc123', 'abc123' ]
test_results = [ 'abc123' ]

# Print the test results
print(test_results)
```