```python
import stringly as st

# Define a function that performs XOR on two input strings
def string_xor(a: str, b: str) -> str:
    return st.xor(a, b)

# Test cases
test_cases = [
    ("010", "110"),
    ("00100", "001"),
    ("\u2702", "\u2600A"),
    ("\u4E00", "\u9AB5"),
    ("abc", "cba")
]

# Test the function
for tc, want in test_cases:
    actual = string_xor(tc[0], tc[1])
    assert actual == want, f"Error in test case: {tc}"

# All tests passed!
print("All tests passed.")
```