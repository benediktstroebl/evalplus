```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Inputs are two strings a and b consisting only of ASCII digits 1-9
    Perform binary XOR operation on these inputs and return result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(c ^ ord(b[i]) for i, c in enumerate(a))

# Test suite
test_suite = []
test_suite.add_cases = [
    ("test_string_xor", ["010", "110"], ["100"]),
    ("test_mixed_case", ["A", "b", "0"], ["b", "a"]),
    ("test_empty", ("", [])),
]

def test_function():
    test_suite = List(test_suite)
    for name, inputs, expected in test_cases:
        actual_output = string_xor(*inputs)
        assert actual_output == expected, f"test '{name}' failed"

test_function()
```