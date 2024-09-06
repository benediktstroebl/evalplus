```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform XOR operation on two strings and return the result as a string.
    Args:
        a (string): The first input string.
        b (string): The second input string.
    Returns:
    str
    """
    # validate inputs
    assert len(a) == len(b)
    assert all(c == chr(0) if c.isdigit() else c for c in a)
    assert all(c == chr(0) if c.isdigit() else c for c in b)
    # perform XOR operation
    return ''.join(map(lambda x: x ^ y, a, b))

# test function with inputs that passes all validation tests
print(string_xor('010', '110'))  # expected output 100
```