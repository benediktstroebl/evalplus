```python
import stringio
from typing import List

def string_xor(a: str, b: str) -> str:
    return "".join(chr((ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

# Test cases
test_cases = [
    "010", "110", "000",
    "001", "101", # Different string lengths
    "1010", # Different character sets
    "0000"
]

for test_case in test_cases:
    actual = string_xor(test_case, test_case)
    assert actual == "100", f"Test case '{test_case} failed: {actual} != '100'."

# Test passing capabilities
print("All tests passed!")
```