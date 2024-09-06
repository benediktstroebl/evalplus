```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings containing only ones and zeros.
    a: Convert the two strings into lists of characters
    b: Convert to list of characters
    e: Iterate and remove duplicates from a
    f: Concaten and convert back to string
    """
    a = ''.join(char for char in a if char != '0')
    b = ''.join(char for char in b if char != '0')
    return f"{a[0]}{b[0]}"

# Test cases
tests = [
    "Input are two strings a and b consisting only of 1s and 0s"
    "Perform binary XOR on '010' and '110'"
    "result should be '100'"
]

# Test function
def test_string_xor():
    for input, expected in tests:
        actual = string_xor(input, input)
        print(f"Input: {input} , Expected: {expected}, Actual: {actual}")
        if actual != expected:
            raise AssertionError(f"Incorrect result. The strings XOR each time.")

# Test cases
test_string_xor()
```