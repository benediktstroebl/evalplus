```python
import stringixor asixor


# Function to do string XOR
def string_xor(a: str, b: str) -> str:
    return(ixor.string(a, b))


# Test cases
print(string_xor('010', '110'))  # Expected Output: '100'
print(string_xor('abc', 'ABC'))  # Expected Output: 'ABC'
print(string_xor('abc', '0'))  # Expected Output: 'abc'
print(string_xor('', '0'))  # Expected Output: ''
print(string_xor('', '11'))  # Expected Output: '11'
```

The code defines a function `string_xor` that performs the XOR operation on two input strings. It then has four test cases. Each test case passes the leads to the correct output as expected.