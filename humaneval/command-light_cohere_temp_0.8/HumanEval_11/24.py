```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting of only ones and zeros
    """
    return "".join("".join([x[i] ^ b[i] for i in range(0, len(a) + len(b))]))

# sample test
test_cases = ["010", "110", "001", "0110", "1000"]
for test_case in test_cases:
    result = string_xor(test_case, test_case)
    print(f"Result: {result})
```  The above function performs a simple XOR operation on two strings, and the result is returned. This script also includes sample test cases to test the function.