```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of ones and zeros.
    a = [x[i] for i, c in enumerate(a)]
    b = [0 if c == '0' else c for c in b]
    return ''.join([0 if c == '1' else c for c in b])

# Test cases
test_cases = [
    "010",
    "110",
    "100",
    "000110",
    "001",
    "1010",
]

test_suite = [
    ("results",) for results in map(string_xor, test_cases)
]

# Print the test results
print(*test_suite)
```