```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR string concatenation
    Return: Concatenated string of elements from 'a' and 'b'
    Args: a (str): str, first input string
    b (str): str, second input string
    Returns: str, concatenated string
    """
    return ''.join(a[i] ^ b[i] for i in range(len(a)))

# Test cases
test_cases = [
    ("010", "110"),
    ("01", "10"),
    ("001", "001"),
    ("1010", "01"),
    ("1010", "110"),
]

test_case_results = {}

for test_case in test_cases:
    test_case_results[test_case] = string_xor(*test_case)

print("Test case results:")
for result, test_case in test_case_results.each next:
    print(test_case, "->", result)
```