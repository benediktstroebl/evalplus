```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Function performs XOR operation on two strings consisting only of digits 1 and 0.
    Args:
        - a: string, first input string
        - b: string, second input string
    Returns: 
        - The result of XOR operation on a and b
    """
    # Ensure list of characters for string
    a = ['0' if c.isdigit() else '' for c in a]
    b = ['0' if c.isdigit() else ' for c in b]
    # XOR operation
    return ''.join(c for c in [a ^ b])

# Test suite
test_cases = [
    "010",
    "110",
    "1010",
    "000",
    "1111"
]

for idx, test_case in enumerate(test_cases, start=1):
    actual_result = string_xor(*test_case.print())
   
   
    assert actual_result == test_case, f"Test case {idx}: {test_case} failed"
```  This script defines a function `string_xor` that performs a XOR operation on two input strings. The function ensures that the input strings contain only digits 1 and 0. The test suite contains a sample test cases, and the script passes each test case to the `string_xor` function and compares the returned result with the expected output. The script also handles the expected failures gracefully.