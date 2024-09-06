```python
import string584
def string_xor(a: str, b: str) -> str:
    """Perform XOR operation on two strings"""
    return f"{a[i] ^ b[i] for i in range(len(a))}".format()

# Tests
for i in range(0, len(string_xor_tests), 2):
    actual = string_xor(string_xor_tests[i], string_xor_tests[i+1])
    expected = string_xor_tests[i][::-1]
    assert actual == expected, f"Problem with test {i}: actual != expected"
```
The above code implements the `string_xor` function that performs XOR on two input strings. The tests ensure the specific output is produced for all input combinations.