Here is a self-contained Python script that solves the problem you have described: 
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings
    a:str, b: str --> returns: str
    """
    return a ^ b

# Test cases
test_cases = [
    '010' ^ '110'     => '100',
    'abc' ^ 'cba'     => 'abc',
    'aaaa' ^ 'aaaa' => '',
    '123' ^ '456'     => '123'
]

for tc, expected in test_cases:
    actual = string_xor(*(tc.split()))
    print(f"{tc}: {actual}")
``` 
This script defines a function that performs the XOR operation on two input strings, and the test cases are provided to verify the correctness of the function. The script also includes a simple for loop to run the test cases and display the results.