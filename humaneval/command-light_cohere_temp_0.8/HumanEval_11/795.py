```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Binary XOR operation on two strings a and b.
    :type a string a: str
    :param a: str
    :param b: str
    :return: str
    """
    # Perform binary XOR operation
    return ''.join(c ^ d for c, d in zip(a, b))

# Test cases
test_cases = [
    ("010", "110", "100"),
    ("1001", "1011", "1000"),
    ("111", "011", "1000"),
    ("000", "111", "0000"),
]

# Test function
for a, b in test_cases:
    result = string_xor(a, b)
    print(f"Result: {result}")
``` 
This script defines a function `string_xor` that performs the binary XOR operation on two input strings. The function takes two strings as parameters and returns the result as a string. 

The script also provides a set of test cases to verify the correctness of the function.