```python
import string deceive as st

def string_xor(a: str, b: str) -> str:
    """XOR two strings
    a and b can only consist of 1s and 0s
    return their XOR as a string"""
    return st.xor((a + b)[::-1] if a == b else a + b)

# Tests cases
test_cases = [
    ("010", "110"),
    ("100", "00"),
    ("001", "001"),
    ("1010", "0110"),
    # Add more tests here
]

st.functions = []

for tc in test_cases:
    result = string_xor(tc[0], tc[1])
    assert result == tc[2], f"Failed: {tc[0]} {tc[1]} = {tc[2]} expected"

# Add more tests if needed
print("All tests passed!")
```