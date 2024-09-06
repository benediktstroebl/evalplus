```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings and return the result as a string
    Args:
        a: string value
        b: string value
    Returns:
        string xor operation result
    """
    return "".join([str[0] ^ str[1] for str in zip(a, b)])

# Test string_xor function with example inputs
test_cases = [("010", "110", "100", "001", "1010", "0111", "1111")

test_results = []
for test_case in test_cases:
    test_results.append(string_xor(test_case, test_case))

# Print the results of the test cases
for result in test_results:
    print(f"Result: {result} ")
```