```python
import stringmatch as sm

def string_xor(a: str, b: str) -> str:
    return sm.xor(a, b)

# Test function
def test_xor() -> None:
    assert string_xor('010', '110') == '100'

# Test suite
test_xor()
```

The code defines a function called `string_xor` that performs a binary XOR operation on two input strings and returns the result as a string. The function is then tested with the `test_xor` function that asserts the correctness of the `string_xor` function with an example usage. 

The `test_xor` function contains an assertion that checks if the result of calling `string_xor` with specific input strings is equal to the expected result '100'.  The `test_xor` function is then called, which executes the test and asserts that the result is correct.